if (!window.ProjectModuleClass) {
    function ProjectModuleClass(projects, rootId) {
        //This node is the only thing that makes this module unique
        this.rootNode = document.getElementById(rootId);
        this.detailNode = this.rootNode.querySelector(".projectModule__detail");

        this.classes = {
            project: "",
        };

        this.detail = {
            title_parent: this.detailNode.querySelector(".projectModule__detail__title"),
            title: this.detailNode.querySelector(".projectModule__detail__title__container"),
            pictures_parent: this.detailNode.querySelector(".projectModule__detail__pictures"),
            pictures: this.detailNode.querySelector(".projectModule__detail__pictures"),
            description_parent: this.detailNode.querySelector(".projectModule__detail__description"),
            description: this.detailNode.querySelector(".projectModule__detail__description__container"),
            pictureDivStr: "projectModule__detail__picture",
            pictureActiveStr: "projectModule__detail__picture__active",
            pictureImgStr: "projectModule__detail__picture__container",
            blurContainer: this.rootNode.querySelector(".projectModule__detail__blur"),
            closeBtn: this.rootNode.querySelector(".projectModule__detail__close"),
            nextBtn: this.rootNode.querySelector(".projectModule__detail__picture__next"),
            prevBtn: this.rootNode.querySelector(".projectModule__detail__picture__prev")
        };

        this.projects = projects || [];
        this.projectIds = $.map(this.projects, function (project) {
            return project.id;
        });
    }
}

if (!ProjectModuleClass.prototype._getProjectById) {
    ProjectModuleClass.prototype._getProjectById = function (projectId) {
        if (this.projects == null || this.projects.length < 1) {
            return null;
        }

        for (var i = 0; i < this.projects.length; i++) {
            var project = this.projects[i];
            if (project.id != null && project.id == projectId) {
                return project;
            }
        }
        return null;
    }
}

if (!ProjectModuleClass.prototype.setActiveProject) {
    ProjectModuleClass.prototype.setActiveProject = function (projectId) {
        var project = this._getProjectById(projectId);
        var dialogAlreadyMounted = !!this.activeProjectDetail;
        this.activeProjectDetail = project;

        if (project == null) {
            this.detail.title.innerText = '';
            this._clearPictures(this.detail.pictures);
            this.detail.description.innerText = '';
            this.detailNode.style.visibility = "hidden";

            // Hide blur
            this.detail.blurContainer.style.display = "none";
            this.detail.closeBtn.style.display = "none";
            return;
        }

        this.detail.pictures.innerHTML = '';
        this.detail.title.innerText = project.name;
        this.detail.description.innerHTML = '<span class="projectModule__detail__description__prefix">' + project.name + ' </span>' + project.description;
        this.changeInfoVisibility(this.detail.description_parent, !this.empty(project.description));

        if (dialogAlreadyMounted || !project) {
            this._clearPictures(this.detail.pictures);
        }

        for (var i = 0; i < project.images.length; i++) {
            this._insertPicture(this.detail.pictures, project.images[i]);
        }
        this.buildCarousel(dialogAlreadyMounted);

        if (!dialogAlreadyMounted) {
            this.detailNode.focus();
            this.detailNode.style.visibility = "inherit";
            this.detail.blurContainer.style.display = "block";
            this.detail.closeBtn.style.display = "block";
            this.calculateClosePosition();
        }
    }
}

if (!ProjectModuleClass.prototype.navigateToAnotherProject) {
    /**
     * Navigate either to the previous or next project.
     * @param goToNextOne boolean If true, move to the next project. Otherwise, it goes to the previous one.
     */
    ProjectModuleClass.prototype.navigateToAnotherProject = function (goToNextOne) {
        if (typeof (goToNextOne) !== "boolean") {
            goToNextOne = true;
        }

        var currentId = this.activeProjectDetail.id;
        var nextId = goToNextOne ? this.getNextProjectId(currentId) : this.getPreviousProjectId(currentId);

        this.setActiveProject(nextId);
    }
}

if (!ProjectModuleClass.prototype.calculateClosePosition) {
    ProjectModuleClass.prototype.calculateClosePosition = function () {
        var rect = this.detailNode.getBoundingClientRect();
        //this.detail.closeBtn.style.top = (rect.top) + "px";
        //this.detail.closeBtn.style.right = ((rect.right - rect.width) + 10) + "px";
    }
}

if (!ProjectModuleClass.prototype.changeInfoVisibility) {
    ProjectModuleClass.prototype.changeInfoVisibility = function (component, visible) {
        if (visible && component == this.detail.description_parent) {
            component.style.display = "flex";
            $('body').addClass("modal-open");
        } else if (visible) {
            component.style.display = "block";
            $('body').addClass("modal-open");
        } else {
            component.style.display = "none";
            $('body').removeClass("modal-open");
        }
    }
}
if (!ProjectModuleClass.prototype.empty) {
    ProjectModuleClass.prototype.empty = function (data) {
        if (typeof (data) == 'number' || typeof (data) == 'boolean') {
            return false;
        }
        if (typeof (data) == 'undefined' || data === null) {
            return true;
        }
        if (typeof (data.length) != 'undefined') {
            return data.length == 0;
        }
        var count = 0;
        for (var i in data) {
            if (data.hasOwnProperty(i)) {
                count++;
            }
        }
        return count == 0;
    }
}

if (!ProjectModuleClass.prototype.closeModal) {
    ProjectModuleClass.prototype.closeModal = function () {
        this.deleteCarousel();
        this.changeInfoVisibility(this.detail.description_parent, false);
        this.setActiveProject(null);
    }
}

if (!ProjectModuleClass.prototype._insertPicture) {
    ProjectModuleClass.prototype._insertPicture = function (parentNode, imageUrl) {
        var div = document.createElement("div");
        div.classList.add(this.detail.pictureDivStr);

        var img = document.createElement("img");
        img.src = imageUrl;
        img.className = this.detail.pictureImgStr;
        div.appendChild(img);

        parentNode.appendChild(div);
    }
}

if (!ProjectModuleClass.prototype._clearPictures) {
    ProjectModuleClass.prototype._clearPictures = function (parentNode) {
        while (parentNode.firstChild) {
            parentNode.removeChild(parentNode.firstChild);
        }
    }
}

if (!ProjectModuleClass.prototype.buildCarousel) {
    ProjectModuleClass.prototype.buildCarousel = function (alreadyMounted) {
        var moreThanOnePicture = false;
        if (!this.empty(this.activeProjectDetail)) {
            moreThanOnePicture = (this.activeProjectDetail.images.length > 1);
        }

        var $owl = $(this.detail.pictures);

        if (alreadyMounted) {
            $owl.owlCarousel("destroy");
        }

        $owl.owlCarousel({
            center: true,
            loop: moreThanOnePicture,
            items: 1,
            navigation: true,
            nav: false,
            dots: true,
            slideSpeed: 300,
            paginationSpeed: 400,
            margin: 2,
            autoplay: true,
            autoplayTimeout: 5000,
            autoplayHoverPause: true
        });
        if (!alreadyMounted) {
            $(this.detail.nextBtn).click(function () {
                this.navigateToAnotherProject(true);
            }.bind(this));

            $(this.detail.prevBtn).click(function () {
                this.navigateToAnotherProject(false);
            }.bind(this));
        }

    }
}

if (!ProjectModuleClass.prototype.deleteCarousel) {
    ProjectModuleClass.prototype.deleteCarousel = function () {
        var $owl = $(this.detail.pictures);
        $owl.owlCarousel("destroy");
        $(this.detail.nextBtn).unbind("click");
        $(this.detail.prevBtn).unbind("click")
    }
}

if (!ProjectModuleClass.prototype.getNextProjectId) {
    ProjectModuleClass.prototype.getNextProjectId = function (projectId) {
        var nextIndex = this.projectIds.indexOf(projectId) + 1;
        if (nextIndex === this.projectIds.length) {
            return this.projectIds[0];
        } else {
            return this.projectIds[nextIndex];
        }
    }
}

if (!ProjectModuleClass.prototype.getPreviousProjectId) {
    ProjectModuleClass.prototype.getPreviousProjectId = function (projectId) {
        var currentIndex = this.projectIds.indexOf(projectId);
        if (currentIndex === 0) {
            return this.projectIds[this.projectIds.length - 1];
        } else
            return this.projectIds[currentIndex - 1];
    }
}