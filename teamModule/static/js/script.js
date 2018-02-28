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


function TeamModuleClass(members) {
    this.infoByDataType = {
        member: {
            className: 'teamModule__team__member',
            idPrefix: 'teamModule__Member',
            iconPrefix: 'teamModule__MemberIcon',
            iconClassName: 'teamModule__memberpanel__icon'
        },
        team: {
            className: 'teamModule__team',
            idPrefix: 'teamModule__Team'
        }
    };
    this.detailIdsMapping = {
        picture: "teamModule__MemberDetailProfilePicture",
        fullName: "teamModule__MemberDetailFullName",
        projects: "teamModule__MemberDetailProjects",
        formation: "teamModule__MemberDetailFormation"
    };

    this.activeDataTypes = {
        member: null,
        team: null
    };

    this.members = members;
    this.membersById = TeamModuleHelper.indexArrayByKey(members, 'id');

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
        var icon = document.getElementById(dataTypeInfo.iconPrefix + member.id);
        if (isPartOfTeam) {
            elem.classList.remove("teamModule--hidden");
            icon.classList.remove("teamModule--hidden");
        } else {
            elem.classList.add("teamModule--hidden");
            icon.classList.add("teamModule--hidden");
        }
    }
};

/**
 *
 * @param id The identifier of the member to show. Pass null or hide the detail window.
 * @private
 */
TeamModuleClass.prototype._loadMemberDetails = function (id) {

    var detailsElem = document.getElementById("teamModule__details__current");
    if (id === null) {
        detailsElem.classList.add("teamModule--hidden");
    } else {
        detailsElem.classList.remove("teamModule--hidden");

        var member = this.membersById[id];
        var mapping = this.detailIdsMapping;
        //Nicest Profile Picture
        document.getElementById(mapping.picture).setAttribute("src",member.profilePicUrl);

        var fullName = member.first_name + " " + member.last_name;
        document.getElementById(mapping.fullName).innerText = fullName;

        var projectElement = document.getElementById(mapping.projects);
        projectElement.innerHTML = '';

        for (proj of member.projects) {
          var para = document.createElement('div');
          var node = document.createTextNode(proj.project_name);
          para.appendChild(node);
          projectElement.appendChild(para);
        }

        //document.getElementById(mapping.projects).innerText = projectName;
        document.getElementById(mapping.formation).innerText = member.formation.name;
    }


};

TeamModuleClass.prototype._setActiveDiv = function (id, dataType, activate) {
    var dataTypeInfo = this.infoByDataType[dataType];

    var activateClass = dataTypeInfo.className + "--active";
    var activateIconClass = dataTypeInfo.iconClassName + "--active";

    var elem = document.getElementById(dataTypeInfo.idPrefix + id);
    var icon = document.getElementById("teamModule__MemberIcon" + id);

    if (activate) {
        elem.classList.add(activateClass);
        if(icon != null){
            icon.classList.add(activateIconClass);
        }
    } else {
        elem.classList.remove(activateClass);
        if(icon != null){
            icon.classList.remove(activateIconClass);
          }
    }
};
