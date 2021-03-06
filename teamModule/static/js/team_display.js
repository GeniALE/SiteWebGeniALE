var windw = this;
if (!$.fn.followDetailToFooter) {
  $.fn.followDetailToFooter = function (detailElem) {
    var $this = this,
      $window = $(windw);

    $window.scroll(function (e) {
      if ($window.width() > 780) {


        var $footer = $('footer').first();
        var topValue = 130;
        var padding = 40;
        var pos = $footer.position().top - $(detailElem).first().height() - topValue - padding;
        if ($window.scrollTop() > pos) {
          $this.css({
            position: 'absolute',
            top: pos + topValue
          });
        } else {
          $this.css({
            position: 'fixed',
            top: topValue + 'px'
          });
        }
      } else {
        $this.css({
          position: 'flex'
        });
      }
    });
  };
}

// Register the instance only if not registered
if (!window._TeamModuleHelper) {
  function _TeamModuleHelper() {

  }
}
if (!_TeamModuleHelper.prototype.indexArrayByKey) {
  _TeamModuleHelper.prototype.indexArrayByKey = function (arr, key) {
    var map = {};
    for (var i = 0; i < arr.length; i++) {
      var entry = arr[i];
      map[entry[key]] = entry;
    }
    return map;
  };
}

if (!window.TeamModuleHelper) {
  TeamModuleHelper = new _TeamModuleHelper();
}

// Register the instance only if not registered
if (!window.TeamModuleClass) {
  function TeamModuleClass(members, teams, rootId, all_members) {
    //This node is the only thing that makes this module unique
    this.rootNode = document.getElementById(rootId);
    this.classByType = {
      member: 'teamModule__team__member',
      memberIcon: 'teamModule__memberpanel__icon',
      team: 'teamModule__team'
    };

    //Mapping of the details nodes
    this.details = {
      container: this.rootNode.querySelector(".teamModule__details"),
      picture: this.rootNode.querySelector(".teamModule__details__picture"),
      fullName: this.rootNode.querySelector(".teamModule__details__fullname"),
      bio: this.rootNode.querySelector(".teamModule__details__bio"),
      projects: this.rootNode.querySelector(".teamModule__details__projects"),
      projectsTitle: this.rootNode.querySelector('.teamModule__details__section__title--projects'),
      teamRoles: this.rootNode.querySelector(".teamModule__details__teams"),
      formation: this.rootNode.querySelector(".teamModule__details__formation"),
      blur: this.rootNode.querySelector(".teamModule__details__blur")
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
    console.log('Members: ' + members);
    this.all_members = all_members
    this.old_members = members;
    this.teams = teams;
    this.teamsById = TeamModuleHelper.indexArrayByKey(teams, 'id');
    this.membersById = TeamModuleHelper.indexArrayByKey(all_members, 'id');
    this.hiddenClass = "teamModule--hidden";
    this.invisibleClass = "teamModule--invisible";
    this.modalOpenClass = "modal-open-mobile-only";

    var detailElem = this.rootNode.querySelector(".teamModule__details__sticky");
    $(detailElem).followDetailToFooter(detailElem);

    //Binding to this
    this.setActiveMember = this.setActiveMember.bind(this);
    this.setActiveTeam = this.setActiveTeam.bind(this);
  }
}

if (!TeamModuleClass.prototype.resetActiveDataType) {
  TeamModuleClass.prototype.resetActiveDataType = function (type) {
    if (this.activeDataTypes.hasOwnProperty(type)) {
      this.activeDataTypes[type] = {
        id: null,
        elem: null
      };
    }
  };
}

if (!TeamModuleClass.prototype.setActiveTeam) {
  TeamModuleClass.prototype.setActiveTeam = function (teamId, elem) {
    if (this.activeDataTypes.team.id === teamId) {
      this.setMemberVisibility(-1);
      this.resetActiveDataType('team');
    } else {
      if (teamId !== null) {
        this.setMemberVisibility(teamId);
      }
      this.activeDataTypes.team.id = teamId;
      this.activeDataTypes.team.elem = elem;
    }

    //Reset active member
    if (this.activeDataTypes.member.id) {
      this.setActiveMember(this.activeDataTypes.member.id);
    }
  };
}

if (!TeamModuleClass.prototype.setActiveMember) {
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
        var currentIconElem = this.rootNode.querySelector("." + this.classByType.memberIcon + this.activeDataTypes.member.id);
        this._setActiveDiv(this.activeDataTypes.member.elem, 'member', false);
        this._setActiveDiv(currentIconElem, 'memberIcon', false);
        this._loadMemberDetails(null);
      }
      if (id !== null) {
        nameElem = nameElem ? nameElem : this.rootNode.querySelector("." + this.classByType.member + id);
        iconElem = iconElem ? iconElem : this.rootNode.querySelector("." + this.classByType.memberIcon + id);
        this._setActiveDiv(nameElem, 'member', true);
        this._setActiveDiv(iconElem, 'memberIcon', true);
        this._loadMemberDetails(id);
      }
      this.activeDataTypes.member.id = id;
      this.activeDataTypes.member.elem = nameElem;
    }
  };
}
if (!TeamModuleClass.prototype.setMemberVisibility) {
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
}

if (!TeamModuleClass.prototype.isPartOfTeam) {
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
}
if (!TeamModuleClass.prototype._loadMemberDetails) {
  /**
   * @private
   */
  TeamModuleClass.prototype._loadMemberDetails = function (memberId) {
    const detailsElem = this.details.container;//this.rootNode.querySelector(".teamModule__details");
    if (memberId === null) {
      detailsElem.classList.add(this.invisibleClass);
      this.details.blur.classList.add(this.invisibleClass);
      document.body.classList.remove(this.modalOpenClass);
    } else {
      detailsElem.classList.remove(this.invisibleClass);
      this.details.blur.classList.remove(this.invisibleClass);
      document.body.classList.add(this.modalOpenClass);

      var member = this.membersById[memberId];
      var mapping = this.details;

      mapping.picture.setAttribute("src", member.image);
      mapping.fullName.innerText = member.first_name + " " + member.last_name;
      mapping.bio.innerText = member.bio;


      // Add teams
      var teamElement = mapping.teamRoles;
      teamElement.innerHTML = '';
      for (var i = 0; i < member.teamRoles.length; i++) {
        var teamRole = member.teamRoles[i];
        var teamName = this.teamsById[teamRole.team].team_name;
        var roleName = teamRole.role;

        var roleContainer = document.createElement('div');
        var node = document.createTextNode(teamName + ' (' + roleName + ')');
        roleContainer.appendChild(node);
        teamElement.appendChild(roleContainer);
      }

      //Add projects
      var projectElement = mapping.projects;
      var projectTitle = mapping.projectsTitle;

      if (member.projects.length > 0) {
        projectTitle.classList.remove(this.hiddenClass);
      } else {
        projectTitle.classList.add(this.hiddenClass);
      }

      projectElement.innerHTML = '';

      for (var i = 0; i < member.projects.length; i++) {
        var project = member.projects[i];
        var projectContainer = document.createElement('div');
        var node = document.createTextNode(project.name);
        projectContainer.appendChild(node);
        projectElement.appendChild(projectContainer);
      }
      mapping.formation.innerText = member.formation.name;
    }
  };
}

if (!TeamModuleClass.prototype._setActiveDiv) {
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

if (!TeamModuleClass.prototype.modalClose) {
  TeamModuleClass.prototype.modalClose = function () {
    this.setActiveMember(this.activeDataTypes.member.id);
  };
}
