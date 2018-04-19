
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
            picture: this.detailNode.querySelector(".projectModule__detail__picture__img"),
            description: this.detailNode.querySelector(".projectModule__detail__description_p"),
            status: this.detailNode.querySelector(".projectModule__detail__status")
        }

        this.projects = projects || [];

        this.activeProjectDetail = null;
    }

    ProjectModuleClass.prototype.setActiveProject = function(projectId){
        var project = this._getProjectById(projectId);
        console.log(project);
        this.activeProjectDetail = project;
        console.log("setActiveProject", projectId);
        if(project == null){
            this.detail.title.innerText = '';
            this.detail.picture.src = '';
            this.detail.description.innerText = '';
            this.detail.status.innerText = '';
            this.detailNode.style.display = "none";
            return;
        }

        this.detail.title.innerText = project.name;
        this.detail.picture.src = project.images[0];
        this.detail.description.innerText = project.description;
        this.detail.status.innerText = project.status_text;

        this.detailNode.style.display = "flex";
        this.detailNode.focus();
    }

    ProjectModuleClass.prototype.onBlurDetail = function(){
        //this.setActiveProject(null);
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

}