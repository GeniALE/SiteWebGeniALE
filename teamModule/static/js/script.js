function TeamModuleClass() {
    this.infoByDataType = {
        member: {
            className: 'teamModule__team__member',
            idPrefix: 'teamModule__Member'
        },
        team: {
            className: 'teamModule__team',
            idPrefix: 'teamModule__Team'
        }
    };

    this.activeDataTypes = {
        member: null,
        team: null
    };

    //This binding
    this.setActiveMember = this.setActiveMember.bind(this);
    this.setActiveTeam = this.setActiveTeam.bind(this);
}

TeamModuleClass.prototype.setActiveTeam = function (id) {
    debugger;
    var currentId;
    if (this.activeDataTypes.team === id) {
        this._setActiveDiv(id, 'team', false);
        this.activeDataTypes.team = null;
    } else {
        if ((currentId = this.activeDataTypes.team) !== null) {
            this._setActiveDiv(currentId, 'team', false);
        }
        if (id !== null) {
            this._setActiveDiv(id, 'team', true);
        }
        this.activeDataTypes.team = id;
    }
};


TeamModuleClass.prototype.setActiveMember = function (id) {
    debugger;
    var currentId;
    if (this.activeDataTypes.member === id) {
        this._setActiveDiv(id, 'member', false);
        this.activeDataTypes.member = null;
    } else {
        if ((currentId = this.activeDataTypes.member) !== null) {
            this._setActiveDiv(currentId, 'member', false);
        }
        if (id !== null) {
            this._setActiveDiv(id, 'member', true);
        }
        this.activeDataTypes.member = id;
    }
};

TeamModuleClass.prototype._loadMemberDetails = function (id) {

};

TeamModuleClass.prototype._setActiveDiv = function (id, dataType, activate) {
    var dataTypeInfo = this.infoByDataType[dataType];
    var dataTypeClass = dataTypeInfo.className;
    var activateClass = dataTypeClass + "--active";
    var elem = document.getElementById(dataTypeInfo.idPrefix + id);

    if (activate) {
        elem.classList.remove(dataTypeClass);
        elem.classList.add(activateClass);
    } else {
        elem.classList.remove(activateClass);
        elem.classList.add(dataTypeClass);
    }
};


var teamModule = new TeamModuleClass();