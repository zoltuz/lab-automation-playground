# coding: utf-8

"""
    Riffyn REST API

    ### Vocabulary Before you begin, please familiarize yourself with our [Glossary of Terms](https://help.riffyn.com/hc/en-us/articles/360045503694). ### Getting Started If you'd like to play around with the API, there are several free GUI tools that will allow you to send requests and receive responses. We suggest using the free app [Postman](https://www.getpostman.com/). ### Authentication Begin with a call the [authenticate](/#api-Authentication-authenticate) endpoint using [HTTP Basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) with your `username` and `password` to retrieve either an API Key or an Access Token. For example:      curl -X POST -u '<username>' https://api.app.riffyn.com/v1/auth -v  You may then use either the API Key or the accessToken for all future requests to the API. For example:      curl -H 'access-token: <ACCESS_TOKEN>' https://api.app.riffyn.com/v1/units -v      curl -H 'api-key: <API_KEY>' https://api.app.riffyn.com/v1/units -v  The tokens' values will be either in the message returned by the `/authenticate` endpoint or in the createApiKey `/auth/api-key` or CreateAccesToken `/auth/access-token` endpoints. The API Key will remain valid until it is deauthorized by revoking it through the Security Settings in the Riffyn App UI. The API Key is best for running scripts and longer lasting interactions with the API. The Access Token will expire automatically and is best suited to granting applications short term access to the Riffyn API. Make your requests by sending the HTTP header `api-key: $API_KEY`, or `access-token: $ACCESS_TOKEN`. In Postman, add your prefered token to the headers under the Headers tab for any request other than the original request to `/authenticate`.  If you are enrolled in MultiFactor Authentication (MFA) the `status` returned by the `/authenticate` endpoint will be `MFA_REQUIRED`. A `passCode`, a `stateToken`, and a `factorId` must be passed to the [/verify](/#api-Authentication-verify) endpoint to complete the authentication process and achieve the `SUCCESS` status. MFA must be managed in the Riffyn App UI.  ### Paging and Sorting The majority of endpoints that return a list of data support paging and sorting through the use of three properties, `limit`,  `offset`, and `sort`. Please see the list of query parameters, displayed below each endpoint's code examples, to see if paging or sorting is supported for that specific endpoint.  Certain endpoints return data that's added frequently, like resources. As a result, you may want filter results on either the maximum or minimum creation timestamp. This will prevent rows from shifting their position from the top of the list, as you scroll though subsequent pages of a multi-page response.  Before querying for the first page, store the current date-time (in memory, a database, a file...). On subsequent pages you *may* include the `before` query parameter, to limit the results to records created before that date-time. E.g. before loading page one, you store the current date time of `2016-10-31T22:00:00Z` (ISO date format). Later, when generating the URL for page two, you *could* limit the results by including the query parameter `before=1477951200000` (epoch timestamp).  ### Postman endpoint examples There is a YAML file with the examples of the request on Riffyn API [Click here](/collection) to get the file. If you don't know how to import the collection file, [here](https://learning.postman.com/docs/postman/collections/data-formats/#importing-postman-data) are the steps. ### Client SDKs You may write your own API client, or you may use one of ours. [Click here](/clients) to select your programming language and download an API client.   # noqa: E501

    OpenAPI spec version: 1.4.0
    Contact: support@riffyn.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AddDataToInputBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'resource_def_id': 'str',
        'property_type_id': 'str',
        'event_group_id': 'str',
        'run_group_id': 'str',
        'run_ids': 'list[str]',
        'component_id': 'str',
        'values': 'list[AddDataToInputBodyValues]',
        'append': 'bool'
    }

    attribute_map = {
        'resource_def_id': 'resourceDefId',
        'property_type_id': 'propertyTypeId',
        'event_group_id': 'eventGroupId',
        'run_group_id': 'runGroupId',
        'run_ids': 'runIds',
        'component_id': 'componentId',
        'values': 'values',
        'append': 'append'
    }

    def __init__(self, resource_def_id=None, property_type_id=None, event_group_id=None, run_group_id=None, run_ids=None, component_id=None, values=None, append=None):  # noqa: E501
        """AddDataToInputBody - a model defined in Swagger"""  # noqa: E501
        self._resource_def_id = None
        self._property_type_id = None
        self._event_group_id = None
        self._run_group_id = None
        self._run_ids = None
        self._component_id = None
        self._values = None
        self._append = None
        self.discriminator = None
        self.resource_def_id = resource_def_id
        self.property_type_id = property_type_id
        if event_group_id is not None:
            self.event_group_id = event_group_id
        self.run_group_id = run_group_id
        self.run_ids = run_ids
        if component_id is not None:
            self.component_id = component_id
        self.values = values
        if append is not None:
            self.append = append

    @property
    def resource_def_id(self):
        """Gets the resource_def_id of this AddDataToInputBody.  # noqa: E501

        ResourceDefs are the `inputs` and `outputs` of the activity (step). A `resourceDefId` is the `_id` of one of those `inputs` or `outputs`.  # noqa: E501

        :return: The resource_def_id of this AddDataToInputBody.  # noqa: E501
        :rtype: str
        """
        return self._resource_def_id

    @resource_def_id.setter
    def resource_def_id(self, resource_def_id):
        """Sets the resource_def_id of this AddDataToInputBody.

        ResourceDefs are the `inputs` and `outputs` of the activity (step). A `resourceDefId` is the `_id` of one of those `inputs` or `outputs`.  # noqa: E501

        :param resource_def_id: The resource_def_id of this AddDataToInputBody.  # noqa: E501
        :type: str
        """
        if resource_def_id is None:
            raise ValueError("Invalid value for `resource_def_id`, must not be `None`")  # noqa: E501

        self._resource_def_id = resource_def_id

    @property
    def property_type_id(self):
        """Gets the property_type_id of this AddDataToInputBody.  # noqa: E501

        The `_id` of the property type, for the property you'd like to add data to. Fixed properties may only be set with a single value.  # noqa: E501

        :return: The property_type_id of this AddDataToInputBody.  # noqa: E501
        :rtype: str
        """
        return self._property_type_id

    @property_type_id.setter
    def property_type_id(self, property_type_id):
        """Sets the property_type_id of this AddDataToInputBody.

        The `_id` of the property type, for the property you'd like to add data to. Fixed properties may only be set with a single value.  # noqa: E501

        :param property_type_id: The property_type_id of this AddDataToInputBody.  # noqa: E501
        :type: str
        """
        if property_type_id is None:
            raise ValueError("Invalid value for `property_type_id`, must not be `None`")  # noqa: E501

        self._property_type_id = property_type_id

    @property
    def event_group_id(self):
        """Gets the event_group_id of this AddDataToInputBody.  # noqa: E501

        The `_id` of the event group for the property you'd like to add data to. You must specify eventIds when using eventGroupId. You cannot specify an eventGroupId for a new event. You cannot add more eventIds than what exists in the eventGroup. When eventGroupId is used `runIds` must be included. `runGroupIds` and `append` cannot be used.  # noqa: E501

        :return: The event_group_id of this AddDataToInputBody.  # noqa: E501
        :rtype: str
        """
        return self._event_group_id

    @event_group_id.setter
    def event_group_id(self, event_group_id):
        """Sets the event_group_id of this AddDataToInputBody.

        The `_id` of the event group for the property you'd like to add data to. You must specify eventIds when using eventGroupId. You cannot specify an eventGroupId for a new event. You cannot add more eventIds than what exists in the eventGroup. When eventGroupId is used `runIds` must be included. `runGroupIds` and `append` cannot be used.  # noqa: E501

        :param event_group_id: The event_group_id of this AddDataToInputBody.  # noqa: E501
        :type: str
        """

        self._event_group_id = event_group_id

    @property
    def run_group_id(self):
        """Gets the run_group_id of this AddDataToInputBody.  # noqa: E501

        The `_id` of the run group you'd like to add data to. `runGroupId` can be used instead of `runIds`. One of `runGroupId` or `runIds` must be provided.  # noqa: E501

        :return: The run_group_id of this AddDataToInputBody.  # noqa: E501
        :rtype: str
        """
        return self._run_group_id

    @run_group_id.setter
    def run_group_id(self, run_group_id):
        """Sets the run_group_id of this AddDataToInputBody.

        The `_id` of the run group you'd like to add data to. `runGroupId` can be used instead of `runIds`. One of `runGroupId` or `runIds` must be provided.  # noqa: E501

        :param run_group_id: The run_group_id of this AddDataToInputBody.  # noqa: E501
        :type: str
        """
        if run_group_id is None:
            raise ValueError("Invalid value for `run_group_id`, must not be `None`")  # noqa: E501

        self._run_group_id = run_group_id

    @property
    def run_ids(self):
        """Gets the run_ids of this AddDataToInputBody.  # noqa: E501

        An array of strings containing a specific list of run `_id`s to add the values to. When `runIds` are defined `runGroupId` will be ignored. One of `runGroupId` or `runIds` must be provided.  # noqa: E501

        :return: The run_ids of this AddDataToInputBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._run_ids

    @run_ids.setter
    def run_ids(self, run_ids):
        """Sets the run_ids of this AddDataToInputBody.

        An array of strings containing a specific list of run `_id`s to add the values to. When `runIds` are defined `runGroupId` will be ignored. One of `runGroupId` or `runIds` must be provided.  # noqa: E501

        :param run_ids: The run_ids of this AddDataToInputBody.  # noqa: E501
        :type: list[str]
        """
        if run_ids is None:
            raise ValueError("Invalid value for `run_ids`, must not be `None`")  # noqa: E501

        self._run_ids = run_ids

    @property
    def component_id(self):
        """Gets the component_id of this AddDataToInputBody.  # noqa: E501

        The `_id` of the component you'd like to add data to. Components are defined in the `inputs` and `outputs` of the activity (step)  # noqa: E501

        :return: The component_id of this AddDataToInputBody.  # noqa: E501
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this AddDataToInputBody.

        The `_id` of the component you'd like to add data to. Components are defined in the `inputs` and `outputs` of the activity (step)  # noqa: E501

        :param component_id: The component_id of this AddDataToInputBody.  # noqa: E501
        :type: str
        """

        self._component_id = component_id

    @property
    def values(self):
        """Gets the values of this AddDataToInputBody.  # noqa: E501

        An array of string values (Immutable properties are single-valued. If multiple values are provided only the first one will be used). For multivalued data, an object with the eventIds and the values to be added. Dates must be in ISO, `2018-08-31T15:53:48.998Z` time format. All other types of values will be parsed and converted to the appropriate data type indicated by the `propertyTypeId`.  # noqa: E501

        :return: The values of this AddDataToInputBody.  # noqa: E501
        :rtype: list[AddDataToInputBodyValues]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this AddDataToInputBody.

        An array of string values (Immutable properties are single-valued. If multiple values are provided only the first one will be used). For multivalued data, an object with the eventIds and the values to be added. Dates must be in ISO, `2018-08-31T15:53:48.998Z` time format. All other types of values will be parsed and converted to the appropriate data type indicated by the `propertyTypeId`.  # noqa: E501

        :param values: The values of this AddDataToInputBody.  # noqa: E501
        :type: list[AddDataToInputBodyValues]
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    @property
    def append(self):
        """Gets the append of this AddDataToInputBody.  # noqa: E501

        Indicates if the `values` should be appended to the existing data or overwrite the existing data for the specified `runsIds`, `runGroupId`, or `activityId`.  (Note: It does not apply to immutable properties.  Immutable properties will always be replaced). Default value is `false`. Append cannot be used when specifying an eventGroupId.   # noqa: E501

        :return: The append of this AddDataToInputBody.  # noqa: E501
        :rtype: bool
        """
        return self._append

    @append.setter
    def append(self, append):
        """Sets the append of this AddDataToInputBody.

        Indicates if the `values` should be appended to the existing data or overwrite the existing data for the specified `runsIds`, `runGroupId`, or `activityId`.  (Note: It does not apply to immutable properties.  Immutable properties will always be replaced). Default value is `false`. Append cannot be used when specifying an eventGroupId.   # noqa: E501

        :param append: The append of this AddDataToInputBody.  # noqa: E501
        :type: bool
        """

        self._append = append

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AddDataToInputBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddDataToInputBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
