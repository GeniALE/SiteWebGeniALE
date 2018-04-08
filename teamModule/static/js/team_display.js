// Register the instance only if not registered
if (!window._TeamModuleHelper) {
    function _TeamModuleHelper() {

    }

    _TeamModuleHelper.prototype.indexArrayByKey = function (arr, key) {
        var map = {};
        for (var i = 0; i < arr.length; i++) {
            var entry = arr[i];
            map[entry[key]] = entry;
        }
        return map;
    };
    TeamModuleHelper = new _TeamModuleHelper();
}

// Register the instance only if not registered
if (!window.TeamModuleClass) {
    function TeamModuleClass(members, rootId) {
        //This node is the only thing that makes this module unique
        this.rootNode = document.getElementById(rootId);
        this.classByType = {
            member: 'teamModule__team__member',
            memberIcon: 'teamModule__memberpanel__icon',
            team: 'teamModule__team'
        };

        //Mapping of the details nodes
        this.details = {
            picture: this.rootNode.querySelector(".teamModule__details__picture"),
            fullName: this.rootNode.querySelector(".teamModule__details__fullname"),
            projects: this.rootNode.querySelector(".teamModule__details__projects"),
            formation: this.rootNode.querySelector(".teamModule__details__formation")
        };

        /**
         * A structure to keep track of the active element
         * @type {{member: {id: number, elem: Element}, team: {id: number, elem: Element}}}
         */
        this.activeDataTypes = {
            member: {
                id: null,
                elem: null
            },
            team: {
                id: null,
                elem: null
            }
        };

        this.members = members;
        this.membersById = TeamModuleHelper.indexArrayByKey(members, 'id');
        this.hiddenClass = "teamModule--hidden";

        //Binding to this
        this.setActiveMember = this.setActiveMember.bind(this);
        this.setActiveTeam = this.setActiveTeam.bind(this);
    }

    TeamModuleClass.prototype.resetActiveDataType = function (type) {
        if (this.activeDataTypes.hasOwnProperty(type)) {
            this.activeDataTypes[type] = {
                id: null,
                elem: null
            };
        }
    };

    TeamModuleClass.prototype.setActiveTeam = function (id, elem) {
        if (this.activeDataTypes.team.id === id) {
            this._setActiveDiv(this.activeDataTypes.team.elem, 'team', false);
            this.setMemberVisibility(-1);
            this.resetActiveDataType('team');
        } else {
            if (this.activeDataTypes.team.id !== null) {
                this._setActiveDiv(this.activeDataTypes.team.elem, 'team', false);
            }
            if (id !== null) {
                this._setActiveDiv(elem, 'team', true);
                this.setMemberVisibility(id);
            }
            this.activeDataTypes.team.id = id;
            this.activeDataTypes.team.elem = elem;
        }
    };


    TeamModuleClass.prototype.setActiveMember = function (id, nameElem, iconElem) {
        if (this.activeDataTypes.member.id === id) {
            nameElem = nameElem ? nameElem : this.rootNode.querySelector('.' + this.classByType.member + id);
            iconElem = iconElem ? iconElem : this.rootNode.querySelector("." + this.classByType.memberIcon + id);
            this._setActiveDiv(nameElem, 'member', false);
            this._setActiveDiv(iconElem, 'memberIcon', false);
            this.resetActiveDataType('member');
            this._loadMemberDetails(null);
        } else {
            if (this.activeDataTypes.member.id !== null) {
                nameElem = nameElem ? nameElem : this.rootNode.querySelector("." + this.classByType.member + this.activeDataTypes.member.id);
                iconElem = iconElem ? iconElem : this.rootNode.querySelector("." + this.classByType.memberIcon + this.activeDataTypes.member.id);
                this._setActiveDiv(this.activeDataTypes.member.elem, 'member', false);
                this._setActiveDiv(iconElem, 'memberIcon', false);
                this._loadMemberDetails(null);
            }
            if (id !== null) {
                nameElem =  nameElem ? nameElem : this.rootNode.querySelector("." + this.classByType.member + id);
                iconElem =  iconElem ? iconElem : this.rootNode.querySelector("." + this.classByType.memberIcon + id);
                this._setActiveDiv(nameElem, 'member', true);
                this._setActiveDiv(iconElem, 'memberIcon', true);
                this._loadMemberDetails(id);
            }
            this.activeDataTypes.member.id = id;
            this.activeDataTypes.member.elem = nameElem;
        }
    };

    TeamModuleClass.prototype.setMemberVisibility = function (teamId) {
        for (var i = 0; i < this.members.length; i++) {
            var member = this.members[i];
            var isPartOfTeam = this.isPartOfTeam(member, teamId);
            var elem = this.rootNode.querySelector("." + this.classByType.member + member.id);
            var icon = this.rootNode.querySelector("." + this.classByType.memberIcon + member.id);
            if (isPartOfTeam) {
                elem.classList.remove(this.hiddenClass);
                icon.classList.remove(this.hiddenClass);
            } else {
                elem.classList.add(this.hiddenClass);
                icon.classList.add(this.hiddenClass);
            }
        }
    };

    TeamModuleClass.prototype.isPartOfTeam = function (member, teamId) {
        if (teamId === -1) {
            return true;
        } else {
            for (var j = 0; j < member.teamRoles.length; j++) {
                var teamRole = member.teamRoles[j];
                if (teamRole.team === teamId) {
                    return true;
                }
            }
            return false;
        }
    };

    /**
     * @private
     */
    TeamModuleClass.prototype._loadMemberDetails = function (memberId) {
        var detailsElem = this.rootNode.querySelector(".teamModule__details");
        if (memberId === null) {
            detailsElem.classList.add(this.hiddenClass);
        } else {
            detailsElem.classList.remove(this.hiddenClass);

            var member = this.membersById[memberId];
            var mapping = this.details;

            mapping.picture.setAttribute("src", member.profilePicUrl);
            mapping.fullName.innerText = member.first_name + " " + member.last_name;

            var projectElement = mapping.projects;
            projectElement.innerHTML = '';

            //Add projects
            for (var i = 0; i < member.projects.length; i++) {
                var project = member.projects[i];
                var projectContainer = document.createElement('div');
                var node = document.createTextNode(project.project_name);
                projectContainer.appendChild(node);
                projectElement.appendChild(projectContainer);
            }
            mapping.formation.innerText = member.formation.name;
        }
    };

    /**
     * @private
     */
    TeamModuleClass.prototype._setActiveDiv = function (elem, dataType, activate) {
        var className = this.classByType[dataType];
        var activateClass = className + "--active";
        if (activate) {
            elem.classList.add(activateClass);
        } else {
            elem.classList.remove(activateClass);
        }
    };
}