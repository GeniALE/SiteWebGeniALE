
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
        //this.detail.picture.src = project.images[0];
        this.detail.description.innerText = project.description;
        this.detail.status.innerText = project.status_text;

        /*if(project.images.length > 1){
            var _this = this;
            var leftButtonDiv = document.createElement("div");
            leftButtonDiv.className = "testleft";
            var leftButton = document.createElement("i");
            leftButton.className = "arrow left";
            leftButtonDiv.appendChild(leftButton);
            leftButtonDiv.onclick = function(){
                _this.previousImage();
            }
            this.detail.pictures.appendChild(leftButtonDiv);

            var rightButtonDiv = document.createElement("div");
            rightButtonDiv.className = "testright";
            var rightButton = document.createElement("i");
            rightButton.className = "arrow right";
            rightButtonDiv.appendChild(rightButton);
            rightButtonDiv.onclick = function(){
                _this.nextImage();
            }
            this.detail.pictures.appendChild(rightButtonDiv);
        }*/

        for(var i = 0; i < project.images.length; i++){
            this._insertPicture(this.detail.pictures, project.images[i], i == 0);
        }

        this.detailNode.style.display = "flex";
        this.detailNode.focus();

        if(project.images.length > 1){
            //this._startSlider();
            this.buildCarousel();
        }
    }

    ProjectModuleClass.prototype.onBlurDetail = function(){
        //this.setActiveProject(null);
        //this._stopSlider();
    }

    ProjectModuleClass.prototype.previousImage = function(){
        var images = this.detail.pictures.getElementsByClassName(this.detail.pictureDivStr);
        var activeIndex = this._getActiveDetailPictureId(images);
        if(activeIndex == null || images.length < 1){
            return;
        }
        images[activeIndex].classList.remove(this.detail.pictureActiveStr);
        if(activeIndex == 0){
            activeIndex = (images.length - 1); 
        } else {
            activeIndex -= 1;
        }
        images[activeIndex].classList.add(this.detail.pictureActiveStr);
    }

    ProjectModuleClass.prototype.nextImage = function(){
        var images = this.detail.pictures.getElementsByClassName(this.detail.pictureDivStr);
        var activeIndex = this._getActiveDetailPictureId(images);
        if(activeIndex == null || images.length < 1){
            return;
        }
        images[activeIndex].classList.remove(this.detail.pictureActiveStr);
        if(activeIndex == (images.length - 1)){
            activeIndex = 0; 
        } else {
            activeIndex += 1;
        }
        images[activeIndex].classList.add(this.detail.pictureActiveStr);
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

    ProjectModuleClass.prototype._getActiveDetailPictureId = function(images){
        var activeIndex = null;
        for(var i = 0; i < images.length; i++){
            if(images[i].classList.contains(this.detail.pictureActiveStr)){
                activeIndex = i;
                break;
            }
        }
        return activeIndex;
    }

    ProjectModuleClass.prototype._insertPicture = function(parentNode, imageUrl, active){
        var div = document.createElement("div");
        div.classList.add(this.detail.pictureDivStr);
        if(active){
            //div.classList.add(this.detail.pictureActiveStr);
        }
        
        var img = document.createElement("img");
        img.src = imageUrl;
        img.className = this.detail.pictureImgStr;
        //div.appendChild(img);

        parentNode.appendChild(img);
    }

    ProjectModuleClass.prototype.buildCarousel = function(){
        $(this.detail.pictures).owlCarousel({
            center: true,
            //loop: true,
            items:1,
            autoWidth:true,
        });
    }

    ProjectModuleClass.prototype._startSlider = function(){
        var _this = this;
        this.sliderTimer = setInterval(function(){
            _this.nextImage();
        }, 3000);
    }

    ProjectModuleClass.prototype._stopSlider = function(){
        if(this.sliderTimer){
            clearInterval(this.sliderTimer);
        }
    }
}