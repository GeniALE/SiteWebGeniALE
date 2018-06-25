
if (!window.ProjectModuleClass) {

    function ProjectModuleClass(projects, rootId){
        //This node is the only thing that makes this module unique
        this.rootNode = document.getElementById(rootId);
        this.detailNode = this.rootNode.querySelector(".projectModule__detail");

        this.classes ={
            project: "",
        };

        this.detail = {
            title_parent : this.detailNode.querySelector(".projectModule__detail__title"),
            title: this.detailNode.querySelector(".projectModule__detail__title__container"),
            pictures_parent : this.detailNode.querySelector(".projectModule__detail__pictures"),
            pictures: this.detailNode.querySelector(".projectModule__detail__pictures"),
            description_parent : this.detailNode.querySelector(".projectModule__detail__description"),
            description: this.detailNode.querySelector(".projectModule__detail__description__container"),
            status_parent: this.detailNode.querySelector(".projectModule__detail__status"),
            status: this.detailNode.querySelector(".projectModule__detail__status__container"),
            link_parent: this.detailNode.querySelector(".projectModule__detail__link"),
            link: this.detailNode.querySelector(".projectModule__detail__link__container"),
            pictureDivStr : "projectModule__detail__picture",
            pictureActiveStr : "projectModule__detail__picture__active",
            pictureImgStr : "projectModule__detail__picture__container",
            blurContainer : this.rootNode.querySelector(".projectModule__detail__blur"),
            closeBtn: this.rootNode.querySelector(".projectModule__detail__close")
        }

        this.projects = projects || [];
    }

    ProjectModuleClass.prototype._getProjectById = function(projectId){ 
        if(this.projects == null || this.projects.length < 1){ 
            return null; 
        } 
 
        for(var i = 0; i < this.projects.length; i++){ 
            var project = this.projects[i]; 
            if(project.id != null && project.id == projectId){ 
                return project; 
            } 
        } 
        return null; 
    } 

    ProjectModuleClass.prototype.setActiveProject = function(projectId){
        var project = this._getProjectById(projectId);
        //console.log(project);
        this.activeProjectDetail = project;
        //console.log("setActiveProject", projectId);
        if(project == null){
            $(this.detail.pictures).owlCarousel('destroy');
            this.detail.title.innerText = '';
            this.detail.pictures.innerHTML = '';
            this.detail.description.innerText = '';
            this.detail.status.innerText = '';
            this.detail.link.href = '';
            this.detail.link.innerText = '';
            this.detailNode.style.visibility = "hidden";
            //hide blur
            this.detail.blurContainer.style.display = "none";
            this.detail.closeBtn.style.display = "none";
            return;
        }

        this.detail.pictures.innerHTML = '';
        this.detail.title.innerText = project.name;
        this.detail.description.innerText = project.description;
        this.showHideInfo(this.detail.description_parent, !this.empty(project.description));
        this.detail.status.innerText = project.status_text;
        this.showHideInfo(this.detail.status_parent, !this.empty(project.status_text));
        this.detail.link.href = project.website;
        this.detail.link.innerText = project.website;
        this.showHideInfo(this.detail.link_parent, !this.empty(project.website));

        for(var i = 0; i < project.images.length; i++){
            this._insertPicture(this.detail.pictures, project.images[i]);
        }
        var _this = this;
        this.detailNode.style.visibility = "inherit";
        this.detailNode.focus();
        this.buildCarousel();
        this.detail.blurContainer.style.display = "block";
        this.detail.closeBtn.style.display = "block";
        this.calculateClosePosition();
    }

    ProjectModuleClass.prototype.calculateClosePosition = function(){
        var rect = this.detailNode.getBoundingClientRect();
        //alert(JSON.stringify(rect));
        this.detail.closeBtn.style.top = (rect.top + 10) + "px";
        this.detail.closeBtn.style.right = ((rect.right - rect.width) + 10) + "px" ;
    }

    ProjectModuleClass.prototype.showHideInfo = function(component, show){
        if(show && component == this.detail.description_parent){
            component.style.display = "contents";
        } else if(show){
            component.style.display = "block";
        } else {
            component.style.display = "none";
        }
    }
    ProjectModuleClass.prototype.empty = function(data)
    {
      if(typeof(data) == 'number' || typeof(data) == 'boolean'){ 
        return false; 
      }
      if(typeof(data) == 'undefined' || data === null){
        return true; 
      }
      if(typeof(data.length) != 'undefined'){
        return data.length == 0;
      }
      var count = 0;
      for(var i in data){
        if(data.hasOwnProperty(i))
        {
          count ++;
        }
      }
      return count == 0;
    }

    ProjectModuleClass.prototype.closeModal = function(){
        this.setActiveProject(null);
    }

    ProjectModuleClass.prototype._insertPicture = function(parentNode, imageUrl){
        var div = document.createElement("div");
        div.classList.add(this.detail.pictureDivStr);

        var img = document.createElement("img");
        img.src = imageUrl;
        img.className = this.detail.pictureImgStr;
        div.appendChild(img);

        parentNode.appendChild(div);
    }

    ProjectModuleClass.prototype.buildCarousel = function(){
        var moreThanOnePicture = false;
        if(!this.empty(this.activeProjectDetail)){
            moreThanOnePicture = (this.activeProjectDetail.images.length > 1);
        }
        $(this.detail.pictures).owlCarousel({
            center: true,
            loop: moreThanOnePicture,
            items:1,
            navigation: false,
            slideSpeed: 300,
            paginationSpeed: 400,
            margin: 1,
            autoplay:true,
            autoplayTimeout:5000,
            autoplayHoverPause:true
        });
    }
}
