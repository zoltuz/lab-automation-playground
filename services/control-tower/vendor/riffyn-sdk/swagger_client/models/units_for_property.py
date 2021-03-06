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


class UnitsForProperty(object):
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
        'id': 'str',
        'basic_unit': 'bool',
        'definition': 'str',
        'definition_base': 'str',
        'description': 'str',
        'name': 'str',
        'notes': 'str',
        'si_unit': 'bool',
        'symbol': 'str',
        'synonyms': 'list[str]',
        'source': 'str',
        'sharable': 'bool',
        'public': 'bool',
        'creator': 'str',
        'created': 'Created'
    }

    attribute_map = {
        'id': '_id',
        'basic_unit': 'basicUnit',
        'definition': 'definition',
        'definition_base': 'definitionBase',
        'description': 'description',
        'name': 'name',
        'notes': 'notes',
        'si_unit': 'siUnit',
        'symbol': 'symbol',
        'synonyms': 'synonyms',
        'source': 'source',
        'sharable': 'sharable',
        'public': 'public',
        'creator': 'creator',
        'created': 'created'
    }

    def __init__(self, id=None, basic_unit=None, definition=None, definition_base=None, description=None, name=None, notes=None, si_unit=None, symbol=None, synonyms=None, source=None, sharable=None, public=None, creator=None, created=None):  # noqa: E501
        """UnitsForProperty - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._basic_unit = None
        self._definition = None
        self._definition_base = None
        self._description = None
        self._name = None
        self._notes = None
        self._si_unit = None
        self._symbol = None
        self._synonyms = None
        self._source = None
        self._sharable = None
        self._public = None
        self._creator = None
        self._created = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if basic_unit is not None:
            self.basic_unit = basic_unit
        if definition is not None:
            self.definition = definition
        if definition_base is not None:
            self.definition_base = definition_base
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if si_unit is not None:
            self.si_unit = si_unit
        if symbol is not None:
            self.symbol = symbol
        if synonyms is not None:
            self.synonyms = synonyms
        if source is not None:
            self.source = source
        if sharable is not None:
            self.sharable = sharable
        if public is not None:
            self.public = public
        if creator is not None:
            self.creator = creator
        if created is not None:
            self.created = created

    @property
    def id(self):
        """Gets the id of this UnitsForProperty.  # noqa: E501

        The unique id of the unit of measurement.  # noqa: E501

        :return: The id of this UnitsForProperty.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UnitsForProperty.

        The unique id of the unit of measurement.  # noqa: E501

        :param id: The id of this UnitsForProperty.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def basic_unit(self):
        """Gets the basic_unit of this UnitsForProperty.  # noqa: E501


        :return: The basic_unit of this UnitsForProperty.  # noqa: E501
        :rtype: bool
        """
        return self._basic_unit

    @basic_unit.setter
    def basic_unit(self, basic_unit):
        """Sets the basic_unit of this UnitsForProperty.


        :param basic_unit: The basic_unit of this UnitsForProperty.  # noqa: E501
        :type: bool
        """

        self._basic_unit = basic_unit

    @property
    def definition(self):
        """Gets the definition of this UnitsForProperty.  # noqa: E501

        Can be a mathematical formula for calculating this unit of measurment from other units of measurement, or a simple definition.  # noqa: E501

        :return: The definition of this UnitsForProperty.  # noqa: E501
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this UnitsForProperty.

        Can be a mathematical formula for calculating this unit of measurment from other units of measurement, or a simple definition.  # noqa: E501

        :param definition: The definition of this UnitsForProperty.  # noqa: E501
        :type: str
        """

        self._definition = definition

    @property
    def definition_base(self):
        """Gets the definition_base of this UnitsForProperty.  # noqa: E501

        The mathematical expression used to calculate this unit of measurement, in terms of base units.  # noqa: E501

        :return: The definition_base of this UnitsForProperty.  # noqa: E501
        :rtype: str
        """
        return self._definition_base

    @definition_base.setter
    def definition_base(self, definition_base):
        """Sets the definition_base of this UnitsForProperty.

        The mathematical expression used to calculate this unit of measurement, in terms of base units.  # noqa: E501

        :param definition_base: The definition_base of this UnitsForProperty.  # noqa: E501
        :type: str
        """

        self._definition_base = definition_base

    @property
    def description(self):
        """Gets the description of this UnitsForProperty.  # noqa: E501

        A brief description of this unit of measurement.  # noqa: E501

        :return: The description of this UnitsForProperty.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UnitsForProperty.

        A brief description of this unit of measurement.  # noqa: E501

        :param description: The description of this UnitsForProperty.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this UnitsForProperty.  # noqa: E501

        The name of the item.  # noqa: E501

        :return: The name of this UnitsForProperty.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UnitsForProperty.

        The name of the item.  # noqa: E501

        :param name: The name of this UnitsForProperty.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this UnitsForProperty.  # noqa: E501


        :return: The notes of this UnitsForProperty.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this UnitsForProperty.


        :param notes: The notes of this UnitsForProperty.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def si_unit(self):
        """Gets the si_unit of this UnitsForProperty.  # noqa: E501

        Indicated if the unit of measurement is a part of the International System of Units.  # noqa: E501

        :return: The si_unit of this UnitsForProperty.  # noqa: E501
        :rtype: bool
        """
        return self._si_unit

    @si_unit.setter
    def si_unit(self, si_unit):
        """Sets the si_unit of this UnitsForProperty.

        Indicated if the unit of measurement is a part of the International System of Units.  # noqa: E501

        :param si_unit: The si_unit of this UnitsForProperty.  # noqa: E501
        :type: bool
        """

        self._si_unit = si_unit

    @property
    def symbol(self):
        """Gets the symbol of this UnitsForProperty.  # noqa: E501

        The symbol that represents the unit of measurement. E.g. `in` for \"inches\", or `mg` for \"milligrams\".  # noqa: E501

        :return: The symbol of this UnitsForProperty.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this UnitsForProperty.

        The symbol that represents the unit of measurement. E.g. `in` for \"inches\", or `mg` for \"milligrams\".  # noqa: E501

        :param symbol: The symbol of this UnitsForProperty.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def synonyms(self):
        """Gets the synonyms of this UnitsForProperty.  # noqa: E501

        An array of synonyms for the unit. In many instances units have multiple abbreviations or spellings.  # noqa: E501

        :return: The synonyms of this UnitsForProperty.  # noqa: E501
        :rtype: list[str]
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms):
        """Sets the synonyms of this UnitsForProperty.

        An array of synonyms for the unit. In many instances units have multiple abbreviations or spellings.  # noqa: E501

        :param synonyms: The synonyms of this UnitsForProperty.  # noqa: E501
        :type: list[str]
        """

        self._synonyms = synonyms

    @property
    def source(self):
        """Gets the source of this UnitsForProperty.  # noqa: E501

        Indicates if the unit is user defined or a system unit. Possible values are `SYSTEM` or `USER_DEFINED`.  # noqa: E501

        :return: The source of this UnitsForProperty.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this UnitsForProperty.

        Indicates if the unit is user defined or a system unit. Possible values are `SYSTEM` or `USER_DEFINED`.  # noqa: E501

        :param source: The source of this UnitsForProperty.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def sharable(self):
        """Gets the sharable of this UnitsForProperty.  # noqa: E501

        Indicates if the unit can be shared with other users.  # noqa: E501

        :return: The sharable of this UnitsForProperty.  # noqa: E501
        :rtype: bool
        """
        return self._sharable

    @sharable.setter
    def sharable(self, sharable):
        """Sets the sharable of this UnitsForProperty.

        Indicates if the unit can be shared with other users.  # noqa: E501

        :param sharable: The sharable of this UnitsForProperty.  # noqa: E501
        :type: bool
        """

        self._sharable = sharable

    @property
    def public(self):
        """Gets the public of this UnitsForProperty.  # noqa: E501

        Indicates if the unit is visible to all users.  # noqa: E501

        :return: The public of this UnitsForProperty.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this UnitsForProperty.

        Indicates if the unit is visible to all users.  # noqa: E501

        :param public: The public of this UnitsForProperty.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def creator(self):
        """Gets the creator of this UnitsForProperty.  # noqa: E501

        The `username` of the user that created this unit.  # noqa: E501

        :return: The creator of this UnitsForProperty.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this UnitsForProperty.

        The `username` of the user that created this unit.  # noqa: E501

        :param creator: The creator of this UnitsForProperty.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def created(self):
        """Gets the created of this UnitsForProperty.  # noqa: E501


        :return: The created of this UnitsForProperty.  # noqa: E501
        :rtype: Created
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this UnitsForProperty.


        :param created: The created of this UnitsForProperty.  # noqa: E501
        :type: Created
        """

        self._created = created

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
        if issubclass(UnitsForProperty, dict):
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
        if not isinstance(other, UnitsForProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
