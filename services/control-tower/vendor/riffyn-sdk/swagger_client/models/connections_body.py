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


class ConnectionsBody(object):
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
        'entity_id': 'str',
        'entity_type': 'str',
        'resource_def_id': 'str',
        'propagate': 'bool'
    }

    attribute_map = {
        'entity_id': 'entityId',
        'entity_type': 'entityType',
        'resource_def_id': 'resourceDefId',
        'propagate': 'propagate'
    }

    def __init__(self, entity_id=None, entity_type=None, resource_def_id=None, propagate=None):  # noqa: E501
        """ConnectionsBody - a model defined in Swagger"""  # noqa: E501
        self._entity_id = None
        self._entity_type = None
        self._resource_def_id = None
        self._propagate = None
        self.discriminator = None
        self.entity_id = entity_id
        self.entity_type = entity_type
        self.resource_def_id = resource_def_id
        if propagate is not None:
            self.propagate = propagate

    @property
    def entity_id(self):
        """Gets the entity_id of this ConnectionsBody.  # noqa: E501

        The `_id` of the activity or group being exported to the enclosing group.  # noqa: E501

        :return: The entity_id of this ConnectionsBody.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this ConnectionsBody.

        The `_id` of the activity or group being exported to the enclosing group.  # noqa: E501

        :param entity_id: The entity_id of this ConnectionsBody.  # noqa: E501
        :type: str
        """
        if entity_id is None:
            raise ValueError("Invalid value for `entity_id`, must not be `None`")  # noqa: E501

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """Gets the entity_type of this ConnectionsBody.  # noqa: E501

        The `type` is either `activity` or `group` being exported to the enclosing group.  # noqa: E501

        :return: The entity_type of this ConnectionsBody.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this ConnectionsBody.

        The `type` is either `activity` or `group` being exported to the enclosing group.  # noqa: E501

        :param entity_type: The entity_type of this ConnectionsBody.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def resource_def_id(self):
        """Gets the resource_def_id of this ConnectionsBody.  # noqa: E501

        The `_id` of the `input` or `output` of the existing activity. It identifies the resource type being exported to the enclosing group for connection.  # noqa: E501

        :return: The resource_def_id of this ConnectionsBody.  # noqa: E501
        :rtype: str
        """
        return self._resource_def_id

    @resource_def_id.setter
    def resource_def_id(self, resource_def_id):
        """Sets the resource_def_id of this ConnectionsBody.

        The `_id` of the `input` or `output` of the existing activity. It identifies the resource type being exported to the enclosing group for connection.  # noqa: E501

        :param resource_def_id: The resource_def_id of this ConnectionsBody.  # noqa: E501
        :type: str
        """
        if resource_def_id is None:
            raise ValueError("Invalid value for `resource_def_id`, must not be `None`")  # noqa: E501

        self._resource_def_id = resource_def_id

    @property
    def propagate(self):
        """Gets the propagate of this ConnectionsBody.  # noqa: E501

        Propagates the connection to parent if it exists. Defaults to true if not set to false.  # noqa: E501

        :return: The propagate of this ConnectionsBody.  # noqa: E501
        :rtype: bool
        """
        return self._propagate

    @propagate.setter
    def propagate(self, propagate):
        """Sets the propagate of this ConnectionsBody.

        Propagates the connection to parent if it exists. Defaults to true if not set to false.  # noqa: E501

        :param propagate: The propagate of this ConnectionsBody.  # noqa: E501
        :type: bool
        """

        self._propagate = propagate

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
        if issubclass(ConnectionsBody, dict):
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
        if not isinstance(other, ConnectionsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
