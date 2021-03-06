# coding: utf-8

# flake8: noqa

"""
    Riffyn REST API

    ### Vocabulary Before you begin, please familiarize yourself with our [Glossary of Terms](https://help.riffyn.com/hc/en-us/articles/360045503694). ### Getting Started If you'd like to play around with the API, there are several free GUI tools that will allow you to send requests and receive responses. We suggest using the free app [Postman](https://www.getpostman.com/). ### Authentication Begin with a call the [authenticate](/#api-Authentication-authenticate) endpoint using [HTTP Basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) with your `username` and `password` to retrieve either an API Key or an Access Token. For example:      curl -X POST -u '<username>' https://api.app.riffyn.com/v1/auth -v  You may then use either the API Key or the accessToken for all future requests to the API. For example:      curl -H 'access-token: <ACCESS_TOKEN>' https://api.app.riffyn.com/v1/units -v      curl -H 'api-key: <API_KEY>' https://api.app.riffyn.com/v1/units -v  The tokens' values will be either in the message returned by the `/authenticate` endpoint or in the createApiKey `/auth/api-key` or CreateAccesToken `/auth/access-token` endpoints. The API Key will remain valid until it is deauthorized by revoking it through the Security Settings in the Riffyn App UI. The API Key is best for running scripts and longer lasting interactions with the API. The Access Token will expire automatically and is best suited to granting applications short term access to the Riffyn API. Make your requests by sending the HTTP header `api-key: $API_KEY`, or `access-token: $ACCESS_TOKEN`. In Postman, add your prefered token to the headers under the Headers tab for any request other than the original request to `/authenticate`.  If you are enrolled in MultiFactor Authentication (MFA) the `status` returned by the `/authenticate` endpoint will be `MFA_REQUIRED`. A `passCode`, a `stateToken`, and a `factorId` must be passed to the [/verify](/#api-Authentication-verify) endpoint to complete the authentication process and achieve the `SUCCESS` status. MFA must be managed in the Riffyn App UI.  ### Paging and Sorting The majority of endpoints that return a list of data support paging and sorting through the use of three properties, `limit`,  `offset`, and `sort`. Please see the list of query parameters, displayed below each endpoint's code examples, to see if paging or sorting is supported for that specific endpoint.  Certain endpoints return data that's added frequently, like resources. As a result, you may want filter results on either the maximum or minimum creation timestamp. This will prevent rows from shifting their position from the top of the list, as you scroll though subsequent pages of a multi-page response.  Before querying for the first page, store the current date-time (in memory, a database, a file...). On subsequent pages you *may* include the `before` query parameter, to limit the results to records created before that date-time. E.g. before loading page one, you store the current date time of `2016-10-31T22:00:00Z` (ISO date format). Later, when generating the URL for page two, you *could* limit the results by including the query parameter `before=1477951200000` (epoch timestamp).  ### Postman endpoint examples There is a YAML file with the examples of the request on Riffyn API [Click here](/collection) to get the file. If you don't know how to import the collection file, [here](https://learning.postman.com/docs/postman/collections/data-formats/#importing-postman-data) are the steps. ### Client SDKs You may write your own API client, or you may use one of ours. [Click here](/clients) to select your programming language and download an API client.   # noqa: E501

    OpenAPI spec version: 1.4.0
    Contact: support@riffyn.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.authentication_api import AuthenticationApi
from swagger_client.api.experiment_api import ExperimentApi
from swagger_client.api.process_api import ProcessApi
from swagger_client.api.process_activity_api import ProcessActivityApi
from swagger_client.api.property_type_api import PropertyTypeApi
from swagger_client.api.resource_api import ResourceApi
from swagger_client.api.resource_type_api import ResourceTypeApi
from swagger_client.api.run_api import RunApi
from swagger_client.api.tag_api import TagApi
from swagger_client.api.task_api import TaskApi
from swagger_client.api.team_api import TeamApi
from swagger_client.api.unit_api import UnitApi
from swagger_client.api.user_api import UserApi
# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.access_token import AccessToken
from swagger_client.models.access_token_body import AccessTokenBody
from swagger_client.models.access_token_info import AccessTokenInfo
from swagger_client.models.accessible_to import AccessibleTo
from swagger_client.models.accessible_to_inner import AccessibleToInner
from swagger_client.models.activities import Activities
from swagger_client.models.activity import Activity
from swagger_client.models.activity_body import ActivityBody
from swagger_client.models.add_batch_data_to_input_body import AddBatchDataToInputBody
from swagger_client.models.add_component_to_resource_body import AddComponentToResourceBody
from swagger_client.models.add_component_to_resource_type import AddComponentToResourceType
from swagger_client.models.add_data_to_input_body import AddDataToInputBody
from swagger_client.models.add_data_to_input_body_values import AddDataToInputBodyValues
from swagger_client.models.add_member_to_team_body import AddMemberToTeamBody
from swagger_client.models.add_property_to_component_of_resource_body import AddPropertyToComponentOfResourceBody
from swagger_client.models.add_property_to_resource_body import AddPropertyToResourceBody
from swagger_client.models.add_property_type_body import AddPropertyTypeBody
from swagger_client.models.add_resource_def_body import AddResourceDefBody
from swagger_client.models.add_resource_type_body import AddResourceTypeBody
from swagger_client.models.api_key import ApiKey
from swagger_client.models.api_keys import ApiKeys
from swagger_client.models.apply_config_body import ApplyConfigBody
from swagger_client.models.apply_config_body_manual_data import ApplyConfigBodyManualData
from swagger_client.models.apply_config_collection_body import ApplyConfigCollectionBody
from swagger_client.models.apply_config_collection_body_manual_data import ApplyConfigCollectionBodyManualData
from swagger_client.models.apply_config_collection_body_manual_data1 import ApplyConfigCollectionBodyManualData1
from swagger_client.models.apply_config_collection_response import ApplyConfigCollectionResponse
from swagger_client.models.apply_config_response import ApplyConfigResponse
from swagger_client.models.auth_response import AuthResponse
from swagger_client.models.auth_response_factors import AuthResponseFactors
from swagger_client.models.auth_response_profile import AuthResponseProfile
from swagger_client.models.body import Body
from swagger_client.models.body1 import Body1
from swagger_client.models.body2 import Body2
from swagger_client.models.body3 import Body3
from swagger_client.models.body4 import Body4
from swagger_client.models.body5 import Body5
from swagger_client.models.body6 import Body6
from swagger_client.models.body7 import Body7
from swagger_client.models.body8 import Body8
from swagger_client.models.comment import Comment
from swagger_client.models.comment_body import CommentBody
from swagger_client.models.comment_deleted import CommentDeleted
from swagger_client.models.comment_media import CommentMedia
from swagger_client.models.comment_media_file_info import CommentMediaFileInfo
from swagger_client.models.comment_message_body import CommentMessageBody
from swagger_client.models.comment_response import CommentResponse
from swagger_client.models.comment_updated import CommentUpdated
from swagger_client.models.comments import Comments
from swagger_client.models.component import Component
from swagger_client.models.component_property_updated import ComponentPropertyUpdated
from swagger_client.models.connect_runs_along_path_body import ConnectRunsAlongPathBody
from swagger_client.models.connection import Connection
from swagger_client.models.connection_line import ConnectionLine
from swagger_client.models.connection_point import ConnectionPoint
from swagger_client.models.connections_body import ConnectionsBody
from swagger_client.models.created import Created
from swagger_client.models.creator import Creator
from swagger_client.models.data_table import DataTable
from swagger_client.models.data_table_metadata import DataTableMetadata
from swagger_client.models.data_tables import DataTables
from swagger_client.models.data_tables_datatables import DataTablesDatatables
from swagger_client.models.data_tables_datatablesdoc import DataTablesDatatablesdoc
from swagger_client.models.deprecated_group import DeprecatedGroup
from swagger_client.models.deprecated_group_entities import DeprecatedGroupEntities
from swagger_client.models.deprecated_group_version import DeprecatedGroupVersion
from swagger_client.models.duplicate_process import DuplicateProcess
from swagger_client.models.enclosing_connection import EnclosingConnection
from swagger_client.models.entities_for_tag import EntitiesForTag
from swagger_client.models.entities_for_tag_inner import EntitiesForTagInner
from swagger_client.models.error import Error
from swagger_client.models.experiment import Experiment
from swagger_client.models.experiment_id import ExperimentId
from swagger_client.models.experiment_modified import ExperimentModified
from swagger_client.models.experiment_overrides import ExperimentOverrides
from swagger_client.models.experiment_summary import ExperimentSummary
from swagger_client.models.experiments import Experiments
from swagger_client.models.file_upload_status_response import FileUploadStatusResponse
from swagger_client.models.group import Group
from swagger_client.models.group_body import GroupBody
from swagger_client.models.group_body_entities import GroupBodyEntities
from swagger_client.models.group_entities import GroupEntities
from swagger_client.models.group_parent import GroupParent
from swagger_client.models.group_version import GroupVersion
from swagger_client.models.groups import Groups
from swagger_client.models.hint import Hint
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.inline_response2001 import InlineResponse2001
from swagger_client.models.inline_response20010 import InlineResponse20010
from swagger_client.models.inline_response20011 import InlineResponse20011
from swagger_client.models.inline_response20012 import InlineResponse20012
from swagger_client.models.inline_response20013 import InlineResponse20013
from swagger_client.models.inline_response20014 import InlineResponse20014
from swagger_client.models.inline_response20015 import InlineResponse20015
from swagger_client.models.inline_response20016 import InlineResponse20016
from swagger_client.models.inline_response20017 import InlineResponse20017
from swagger_client.models.inline_response20018 import InlineResponse20018
from swagger_client.models.inline_response20019 import InlineResponse20019
from swagger_client.models.inline_response2002 import InlineResponse2002
from swagger_client.models.inline_response2003 import InlineResponse2003
from swagger_client.models.inline_response2004 import InlineResponse2004
from swagger_client.models.inline_response2005 import InlineResponse2005
from swagger_client.models.inline_response2006 import InlineResponse2006
from swagger_client.models.inline_response2007 import InlineResponse2007
from swagger_client.models.inline_response2008 import InlineResponse2008
from swagger_client.models.inline_response2009 import InlineResponse2009
from swagger_client.models.inline_response404 import InlineResponse404
from swagger_client.models.invalid_experiment_id import InvalidExperimentID
from swagger_client.models.invalid_experiment_id_or_activity_id import InvalidExperimentIdOrActivityId
from swagger_client.models.invalid_experiment_id_or_group_id import InvalidExperimentIdOrGroupID
from swagger_client.models.invalid_porperty_type_id_or_unit_id import InvalidPorpertyTypeIdOrUnitId
from swagger_client.models.invalid_process_id import InvalidProcessId
from swagger_client.models.invalid_property_type_id import InvalidPropertyTypeID
from swagger_client.models.invalid_property_type_id_or_user_id import InvalidPropertyTypeIdOrUserId
from swagger_client.models.invalid_resource_id import InvalidResourceId
from swagger_client.models.invalid_resource_type_id import InvalidResourceTypeId
from swagger_client.models.invalid_tag_id import InvalidTagID
from swagger_client.models.invalid_task_id import InvalidTaskID
from swagger_client.models.invalid_team_id import InvalidTeamID
from swagger_client.models.invalid_team_id_or_principal_id import InvalidTeamIdOrPrincipalId
from swagger_client.models.invalid_team_id_or_user_id import InvalidTeamIdOrUserID
from swagger_client.models.invalid_unit_id import InvalidUnitID
from swagger_client.models.links import Links
from swagger_client.models.meta import Meta
from swagger_client.models.modified import Modified
from swagger_client.models.modified_by import ModifiedBy
from swagger_client.models.new_api_key import NewApiKey
from swagger_client.models.new_api_key_body import NewApiKeyBody
from swagger_client.models.new_experiment_body import NewExperimentBody
from swagger_client.models.new_experiment_body_options import NewExperimentBodyOptions
from swagger_client.models.new_property_type_body import NewPropertyTypeBody
from swagger_client.models.new_property_type_body_parents import NewPropertyTypeBodyParents
from swagger_client.models.new_property_unit_body import NewPropertyUnitBody
from swagger_client.models.new_resource_body import NewResourceBody
from swagger_client.models.new_resource_body_components import NewResourceBodyComponents
from swagger_client.models.new_resource_body_properties import NewResourceBodyProperties
from swagger_client.models.new_resource_type_body import NewResourceTypeBody
from swagger_client.models.new_resource_type_body_components import NewResourceTypeBodyComponents
from swagger_client.models.new_resource_type_body_parents import NewResourceTypeBodyParents
from swagger_client.models.new_resource_type_body_properties import NewResourceTypeBodyProperties
from swagger_client.models.new_run_group_body import NewRunGroupBody
from swagger_client.models.new_runs_body import NewRunsBody
from swagger_client.models.new_runs_body_options import NewRunsBodyOptions
from swagger_client.models.new_team_body import NewTeamBody
from swagger_client.models.new_unit_body import NewUnitBody
from swagger_client.models.notfound import Notfound
from swagger_client.models.notfound_alt import NotfoundAlt
from swagger_client.models.one_ofinline_response404 import OneOfinlineResponse404
from swagger_client.models.org import Org
from swagger_client.models.org_inner import OrgInner
from swagger_client.models.permissions import Permissions
from swagger_client.models.process import Process
from swagger_client.models.processes import Processes
from swagger_client.models.propagate_runs_body import PropagateRunsBody
from swagger_client.models.property_added_to_component import PropertyAddedToComponent
from swagger_client.models.property_added_to_resource import PropertyAddedToResource
from swagger_client.models.property_def import PropertyDef
from swagger_client.models.property_def_unit import PropertyDefUnit
from swagger_client.models.property_rule import PropertyRule
from swagger_client.models.property_spec import PropertySpec
from swagger_client.models.property_type import PropertyType
from swagger_client.models.property_types import PropertyTypes
from swagger_client.models.property_updated import PropertyUpdated
from swagger_client.models.public import Public
from swagger_client.models.request_entity_large import RequestEntityLarge
from swagger_client.models.resource import Resource
from swagger_client.models.resource_def import ResourceDef
from swagger_client.models.resource_def_id import ResourceDefId
from swagger_client.models.resource_status import ResourceStatus
from swagger_client.models.resource_status_inner import ResourceStatusInner
from swagger_client.models.resource_type import ResourceType
from swagger_client.models.resource_type_parents import ResourceTypeParents
from swagger_client.models.resource_type_status import ResourceTypeStatus
from swagger_client.models.resource_type_status_inner import ResourceTypeStatusInner
from swagger_client.models.resource_types import ResourceTypes
from swagger_client.models.resources import Resources
from swagger_client.models.resources_components import ResourcesComponents
from swagger_client.models.resources_data import ResourcesData
from swagger_client.models.resources_properties import ResourcesProperties
from swagger_client.models.role import Role
from swagger_client.models.run import Run
from swagger_client.models.run_data_response import RunDataResponse
from swagger_client.models.run_data_response_inner import RunDataResponseInner
from swagger_client.models.run_group import RunGroup
from swagger_client.models.run_groups import RunGroups
from swagger_client.models.run_paths import RunPaths
from swagger_client.models.run_paths_inner import RunPathsInner
from swagger_client.models.run_resource_def import RunResourceDef
from swagger_client.models.run_status import RunStatus
from swagger_client.models.runs import Runs
from swagger_client.models.set_resource_body import SetResourceBody
from swagger_client.models.set_run_overrides_body import SetRunOverridesBody
from swagger_client.models.share_experiment_body import ShareExperimentBody
from swagger_client.models.share_process_body import ShareProcessBody
from swagger_client.models.share_property_type_body import SharePropertyTypeBody
from swagger_client.models.share_resource_body import ShareResourceBody
from swagger_client.models.share_resource_type_body import ShareResourceTypeBody
from swagger_client.models.share_team_body import ShareTeamBody
from swagger_client.models.share_unit_body import ShareUnitBody
from swagger_client.models.shareable import Shareable
from swagger_client.models.spec import Spec
from swagger_client.models.spec_inner import SpecInner
from swagger_client.models.success_added_member import SuccessAddedMember
from swagger_client.models.success_message import SuccessMessage
from swagger_client.models.success_shared import SuccessShared
from swagger_client.models.successfully_connection import SuccessfullyConnection
from swagger_client.models.successfully_creation import SuccessfullyCreation
from swagger_client.models.successfully_delete import SuccessfullyDelete
from swagger_client.models.successfully_exported import SuccessfullyExported
from swagger_client.models.successfully_share import SuccessfullyShare
from swagger_client.models.successfully_unshared import SuccessfullyUnshared
from swagger_client.models.summary_body import SummaryBody
from swagger_client.models.summary_deleted import SummaryDeleted
from swagger_client.models.summary_response import SummaryResponse
from swagger_client.models.tag import Tag
from swagger_client.models.tag_body import TagBody
from swagger_client.models.tag_remove import TagRemove
from swagger_client.models.tags import Tags
from swagger_client.models.task import Task
from swagger_client.models.task_args import TaskArgs
from swagger_client.models.task_list_item import TaskListItem
from swagger_client.models.task_list_item_results import TaskListItemResults
from swagger_client.models.task_metadata import TaskMetadata
from swagger_client.models.task_results import TaskResults
from swagger_client.models.task_status import TaskStatus
from swagger_client.models.team import Team
from swagger_client.models.team_remove import TeamRemove
from swagger_client.models.team_with_members import TeamWithMembers
from swagger_client.models.team_with_members_members import TeamWithMembersMembers
from swagger_client.models.teams import Teams
from swagger_client.models.top_group import TopGroup
from swagger_client.models.unanthorized import Unanthorized
from swagger_client.models.unauthorized import Unauthorized
from swagger_client.models.unit import Unit
from swagger_client.models.unit_removed import UnitRemoved
from swagger_client.models.units import Units
from swagger_client.models.units_for_property import UnitsForProperty
from swagger_client.models.unset_run_overrides_body import UnsetRunOverridesBody
from swagger_client.models.unshare_experiment_body import UnshareExperimentBody
from swagger_client.models.unshare_process_body import UnshareProcessBody
from swagger_client.models.unshare_property_type_body import UnsharePropertyTypeBody
from swagger_client.models.unshare_resource_body import UnshareResourceBody
from swagger_client.models.unshare_resource_type_body import UnshareResourceTypeBody
from swagger_client.models.unshare_team_body import UnshareTeamBody
from swagger_client.models.unshare_unit_body import UnshareUnitBody
from swagger_client.models.update_activity_body import UpdateActivityBody
from swagger_client.models.update_api_key_response import UpdateApiKeyResponse
from swagger_client.models.update_component_on_res_type import UpdateComponentOnResType
from swagger_client.models.update_experiment_body import UpdateExperimentBody
from swagger_client.models.update_group_body import UpdateGroupBody
from swagger_client.models.update_process import UpdateProcess
from swagger_client.models.update_property_of_component_of_resource_body import UpdatePropertyOfComponentOfResourceBody
from swagger_client.models.update_property_of_resource_body import UpdatePropertyOfResourceBody
from swagger_client.models.update_property_type_body import UpdatePropertyTypeBody
from swagger_client.models.update_property_type_body_parents import UpdatePropertyTypeBodyParents
from swagger_client.models.update_resource_body import UpdateResourceBody
from swagger_client.models.update_resource_body_components import UpdateResourceBodyComponents
from swagger_client.models.update_resource_body_properties import UpdateResourceBodyProperties
from swagger_client.models.update_resource_type_body import UpdateResourceTypeBody
from swagger_client.models.update_resource_type_body_components import UpdateResourceTypeBodyComponents
from swagger_client.models.update_resource_type_body_properties import UpdateResourceTypeBodyProperties
from swagger_client.models.update_run_body import UpdateRunBody
from swagger_client.models.update_run_status_body import UpdateRunStatusBody
from swagger_client.models.update_team_body import UpdateTeamBody
from swagger_client.models.update_unit_body import UpdateUnitBody
from swagger_client.models.upload_config import UploadConfig
from swagger_client.models.upload_config_activities import UploadConfigActivities
from swagger_client.models.upload_config_collection import UploadConfigCollection
from swagger_client.models.upload_config_collection_manual_data import UploadConfigCollectionManualData
from swagger_client.models.upload_config_collection_parse_configs import UploadConfigCollectionParseConfigs
from swagger_client.models.upload_config_collection_target import UploadConfigCollectionTarget
from swagger_client.models.upload_config_collections import UploadConfigCollections
from swagger_client.models.upload_config_manual_data import UploadConfigManualData
from swagger_client.models.upload_config_target import UploadConfigTarget
from swagger_client.models.upload_configs import UploadConfigs
from swagger_client.models.upload_file_response import UploadFileResponse
from swagger_client.models.user import User
from swagger_client.models.user_emails import UserEmails
from swagger_client.models.user_profile import UserProfile
from swagger_client.models.users import Users
from swagger_client.models.verify_body import VerifyBody
from swagger_client.models.verify_response import VerifyResponse
from swagger_client.models.version import Version
