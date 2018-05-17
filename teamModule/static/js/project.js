
if (!window.ProjectModuleClass) {

    function ProjectModuleClass(projects, rootId){
        //This node is the only thing that makes this module unique
        this.rootNode = document.getElementById(rootId);
        this.detailNode = this.rootNode.querySelector(".projectModule__detail");

        this.classes ={
            project: "",
        };

        this.detail = {
            title: this.detailNode.querySelector(".projectModule__detail__title__h"),
            pictures: this.detailNode.querySelector(".projectModule__detail__pictures"),
            description: this.detailNode.querySelector(".projectModule__detail__description_p"),
            status: this.detailNode.querySelector(".projectModule__detail__status"),
            pictureDivStr : "projectModule__detail__picture",
            pictureActiveStr : "projectModule__detail__picture__active",
            pictureImgStr : "projectModule__detail__picture__img"
        }

        this.projects = projects || [];

        //this.activeProjectDetail = null;
        this.sliderTimer = null;
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
        console.log(project);
        this.activeProjectDetail = project;
        console.log("setActiveProject", projectId);
        if(project == null){
            this.detail.title.innerText = '';
            this.detail.pictures.innerHTML = '';
            this.detail.description.innerText = '';
            this.detail.status.innerText = '';
            this.detailNode.style.display = "none";
            return;
        }

        this.detail.pictures.innerHTML = '';
        this.detail.title.innerText = project.name;
        this.detail.description.innerText = project.description;
        this.detail.status.innerText = project.status_text;

        for(var i = 0; i < project.images.length; i++){
            this._insertPicture(this.detail.pictures, project.images[i]);
        }
        var _this = this;
        this.detailNode.style.display = "flex";
        this.detailNode.focus();
        setTimeout(() => {
            this.buildCarousel();
        }, 100);
    }

    ProjectModuleClass.prototype.onBlurDetail = function(){
        //$(this.detail.pictures).owlCarousel('destroy');
        //this.setActiveProject(null);
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
        $(this.detail.pictures).owlCarousel({
            center: true,
            //loop: true,
            items:1,
            navigation: true, // Show next and prev buttons
            slideSpeed: 300,
            paginationSpeed: 400,
            //margin: 1,
        });
    }
}
