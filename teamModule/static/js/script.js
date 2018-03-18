//Look, this is how we do a class in ES5
function TeamModuleHelper() {

}

TeamModuleHelper.prototype.indexArrayByKey = function (arr, key) {
    var map = {};
    for (var i = 0; i < arr.length; i++) {
        var entry = arr[i];
        map[entry[key]] = entry;
    }
    return map;
};

var TeamModuleHelper = new TeamModuleHelper();

function TeamModuleClass(members, idSuffix, cssPrefix) {
    this.infoByDataType = {
        member: {
            className: cssPrefix + 'teamModule__team__member',
            idPrefix: 'teamModule__Member' + idSuffix,
            iconIdPrefix: 'teamModule__MemberIcon' + idSuffix,
            iconClassName: cssPrefix + 'teamModule__memberpanel__icon'
        },
        team: {
            className: cssPrefix + 'teamModule__team',
            idPrefix: 'teamModule__Team' + idSuffix
        }
    };
    this.detailIdsMapping = {
        picture: "teamModule__MemberDetailProfilePicture" + idSuffix,
        fullName: "teamModule__MemberDetailFullName" + idSuffix,
        projects: "teamModule__MemberDetailProjects" + idSuffix,
        formation: "teamModule__MemberDetailFormation" + idSuffix
    };

    this.activeDataTypes = {
        member: null,
        team: null
    };

    this.members = members;
    this.membersById = TeamModuleHelper.indexArrayByKey(members, 'id');

    //Misc
    this.currentDetailId = "teamModule__details__current" + idSuffix;
    this.hiddenClass = cssPrefix + "teamModule--hidden";

    //This binding
    this.setActiveMember = this.setActiveMember.bind(this);
    this.setActiveTeam = this.setActiveTeam.bind(this);
}

TeamModuleClass.prototype.setActiveTeam = function (id) {
    var currentId;
    if (this.activeDataTypes.team === id) {
        this._setActiveDiv(id, 'team', false);
        this.setMemberVisibility(-1);
        this.activeDataTypes.team = null;
    } else {
        if ((currentId = this.activeDataTypes.team) !== null) {
            this._setActiveDiv(currentId, 'team', false);
        }
        if (id !== null) {
            this._setActiveDiv(id, 'team', true);
            this.setMemberVisibility(id);
        }
        this.activeDataTypes.team = id;
    }
};


TeamModuleClass.prototype.setActiveMember = function (id) {
    var currentId;
    if (this.activeDataTypes.member === id) {
        this._setActiveDiv(id, 'member', false);
        this.activeDataTypes.member = null;
        this._loadMemberDetails(null);
    } else {
        if ((currentId = this.activeDataTypes.member) !== null) {
            this._setActiveDiv(currentId, 'member', false);
            this._loadMemberDetails(null);
        }
        if (id !== null) {
            this._setActiveDiv(id, 'member', true);
            this._loadMemberDetails(id);
        }
        this.activeDataTypes.member = id;
    }
};

TeamModuleClass.prototype.setMemberVisibility = function (teamId) {
    var dataTypeInfo = this.infoByDataType.member;
    for (var i = 0; i < this.members.length; i++) {
        var member = this.members[i];

        var isPartOfTeam = false;

        if (teamId === -1) {
            isPartOfTeam = true;
        } else {
            for (var j = 0; j < member.teamRoles.length; j++) {
                var teamRole = member.teamRoles[j];
                if (teamRole.team === teamId) {
                    isPartOfTeam = true;
                    break;
                }
            }
        }

        var elem = document.getElementById(dataTypeInfo.idPrefix + member.id);
        var icon = document.getElementById(dataTypeInfo.iconIdPrefix + member.id);
        if (isPartOfTeam) {
            elem.classList.remove(this.hiddenClass);
            icon.classList.remove(this.hiddenClass);
        } else {
            elem.classList.add(this.hiddenClass);
            icon.classList.add(this.hiddenClass);
        }
    }
};

/**
 *
 * @param id The identifier of the member to show. Pass null or hide the detail window.
 * @private
 */
TeamModuleClass.prototype._loadMemberDetails = function (id) {

    var detailsElem = document.getElementById(this.currentDetailId);
    if (id === null) {
        detailsElem.classList.add(this.hiddenClass);
    } else {
        detailsElem.classList.remove(this.hiddenClass);

        var member = this.membersById[id];
        var mapping = this.detailIdsMapping;
        //Nicest Profile Picture
        document.getElementById(mapping.picture).setAttribute("src", member.profilePicUrl);
        document.getElementById(mapping.fullName).innerText = member.first_name + " " + member.last_name;

        var projectElement = document.getElementById(mapping.projects);
        projectElement.innerHTML = '';

        for (var i = 0; i < member.projects.length; i++) {
            var proj = member.projects[i];
            var projectContainer = document.createElement('div');
            var node = document.createTextNode(proj.project_name);
            projectContainer.appendChild(node);
            projectElement.appendChild(projectContainer);
        }
        document.getElementById(mapping.formation).innerText = member.formation.name;
    }
};

TeamModuleClass.prototype._setActiveDiv = function (id, dataType, activate) {
    var dataTypeInfo = this.infoByDataType[dataType];

    var activateClass = dataTypeInfo.className + "--active";
    var activateIconClass = dataTypeInfo.iconClassName + "--active";

    var elem = document.getElementById(dataTypeInfo.idPrefix + id);
    var icon = document.getElementById(dataTypeInfo.iconIdPrefix + id);

    if (activate) {
        elem.classList.add(activateClass);
        if (icon != null) {
            icon.classList.add(activateIconClass);
        }
    } else {
        elem.classList.remove(activateClass);
        if (icon != null) {
            icon.classList.remove(activateIconClass);
        }
    }
};
