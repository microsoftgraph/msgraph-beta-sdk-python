from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
activity_settings = lazy_import('msgraph.generated.models.external_connectors.activity_settings')
compliance_settings = lazy_import('msgraph.generated.models.external_connectors.compliance_settings')
configuration = lazy_import('msgraph.generated.models.external_connectors.configuration')
connection_operation = lazy_import('msgraph.generated.models.external_connectors.connection_operation')
connection_quota = lazy_import('msgraph.generated.models.external_connectors.connection_quota')
connection_state = lazy_import('msgraph.generated.models.external_connectors.connection_state')
content_experience_type = lazy_import('msgraph.generated.models.external_connectors.content_experience_type')
external_group = lazy_import('msgraph.generated.models.external_connectors.external_group')
external_item = lazy_import('msgraph.generated.models.external_connectors.external_item')
schema = lazy_import('msgraph.generated.models.external_connectors.schema')
search_settings = lazy_import('msgraph.generated.models.external_connectors.search_settings')

class ExternalConnection(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def activity_settings(self,) -> Optional[activity_settings.ActivitySettings]:
        """
        Gets the activitySettings property value. Collects configurable settings related to activities involving connector content.
        Returns: Optional[activity_settings.ActivitySettings]
        """
        return self._activity_settings
    
    @activity_settings.setter
    def activity_settings(self,value: Optional[activity_settings.ActivitySettings] = None) -> None:
        """
        Sets the activitySettings property value. Collects configurable settings related to activities involving connector content.
        Args:
            value: Value to set for the activitySettings property.
        """
        self._activity_settings = value
    
    @property
    def compliance_settings(self,) -> Optional[compliance_settings.ComplianceSettings]:
        """
        Gets the complianceSettings property value. The settings required for the connection to participate in eDiscovery, such as the display templates for eDiscovery results.
        Returns: Optional[compliance_settings.ComplianceSettings]
        """
        return self._compliance_settings
    
    @compliance_settings.setter
    def compliance_settings(self,value: Optional[compliance_settings.ComplianceSettings] = None) -> None:
        """
        Sets the complianceSettings property value. The settings required for the connection to participate in eDiscovery, such as the display templates for eDiscovery results.
        Args:
            value: Value to set for the complianceSettings property.
        """
        self._compliance_settings = value
    
    @property
    def configuration(self,) -> Optional[configuration.Configuration]:
        """
        Gets the configuration property value. Specifies additional application IDs that are allowed to manage the connection and to index content in the connection. Optional.
        Returns: Optional[configuration.Configuration]
        """
        return self._configuration
    
    @configuration.setter
    def configuration(self,value: Optional[configuration.Configuration] = None) -> None:
        """
        Sets the configuration property value. Specifies additional application IDs that are allowed to manage the connection and to index content in the connection. Optional.
        Args:
            value: Value to set for the configuration property.
        """
        self._configuration = value
    
    @property
    def connector_id(self,) -> Optional[str]:
        """
        Gets the connectorId property value. The Teams App ID. Optional.
        Returns: Optional[str]
        """
        return self._connector_id
    
    @connector_id.setter
    def connector_id(self,value: Optional[str] = None) -> None:
        """
        Sets the connectorId property value. The Teams App ID. Optional.
        Args:
            value: Value to set for the connectorId property.
        """
        self._connector_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new externalConnection and sets the default values.
        """
        super().__init__()
        # Collects configurable settings related to activities involving connector content.
        self._activity_settings: Optional[activity_settings.ActivitySettings] = None
        # The settings required for the connection to participate in eDiscovery, such as the display templates for eDiscovery results.
        self._compliance_settings: Optional[compliance_settings.ComplianceSettings] = None
        # Specifies additional application IDs that are allowed to manage the connection and to index content in the connection. Optional.
        self._configuration: Optional[configuration.Configuration] = None
        # The Teams App ID. Optional.
        self._connector_id: Optional[str] = None
        # Description of the connection displayed in the Microsoft 365 admin center. Optional.
        self._description: Optional[str] = None
        # The list of content experiences the connection will participate in. Possible values are search and compliance.
        self._enabled_content_experiences: Optional[content_experience_type.ContentExperienceType] = None
        # The groups property
        self._groups: Optional[List[external_group.ExternalGroup]] = None
        # The number of items ingested into a connection. This value is refreshed every 15 minutes. If the connection state is draft, then ingestedItemsCount will be null.
        self._ingested_items_count: Optional[int] = None
        # The items property
        self._items: Optional[List[external_item.ExternalItem]] = None
        # The display name of the connection to be displayed in the Microsoft 365 admin center. Maximum length of 128 characters. Required.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The operations property
        self._operations: Optional[List[connection_operation.ConnectionOperation]] = None
        # The quota property
        self._quota: Optional[connection_quota.ConnectionQuota] = None
        # The schema property
        self._schema: Optional[schema.Schema] = None
        # The settings configuring the search experience for content in this connection, such as the display templates for search results.
        self._search_settings: Optional[search_settings.SearchSettings] = None
        # Indicates the current state of the connection. Possible values are draft, ready, obsolete, and limitExceeded. Required.
        self._state: Optional[connection_state.ConnectionState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExternalConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExternalConnection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExternalConnection()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the connection displayed in the Microsoft 365 admin center. Optional.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the connection displayed in the Microsoft 365 admin center. Optional.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def enabled_content_experiences(self,) -> Optional[content_experience_type.ContentExperienceType]:
        """
        Gets the enabledContentExperiences property value. The list of content experiences the connection will participate in. Possible values are search and compliance.
        Returns: Optional[content_experience_type.ContentExperienceType]
        """
        return self._enabled_content_experiences
    
    @enabled_content_experiences.setter
    def enabled_content_experiences(self,value: Optional[content_experience_type.ContentExperienceType] = None) -> None:
        """
        Sets the enabledContentExperiences property value. The list of content experiences the connection will participate in. Possible values are search and compliance.
        Args:
            value: Value to set for the enabledContentExperiences property.
        """
        self._enabled_content_experiences = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "activity_settings": lambda n : setattr(self, 'activity_settings', n.get_object_value(activity_settings.ActivitySettings)),
            "compliance_settings": lambda n : setattr(self, 'compliance_settings', n.get_object_value(compliance_settings.ComplianceSettings)),
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(configuration.Configuration)),
            "connector_id": lambda n : setattr(self, 'connector_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "enabled_content_experiences": lambda n : setattr(self, 'enabled_content_experiences', n.get_enum_value(content_experience_type.ContentExperienceType)),
            "groups": lambda n : setattr(self, 'groups', n.get_collection_of_object_values(external_group.ExternalGroup)),
            "ingested_items_count": lambda n : setattr(self, 'ingested_items_count', n.get_int_value()),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(external_item.ExternalItem)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(connection_operation.ConnectionOperation)),
            "quota": lambda n : setattr(self, 'quota', n.get_object_value(connection_quota.ConnectionQuota)),
            "schema": lambda n : setattr(self, 'schema', n.get_object_value(schema.Schema)),
            "search_settings": lambda n : setattr(self, 'search_settings', n.get_object_value(search_settings.SearchSettings)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(connection_state.ConnectionState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def groups(self,) -> Optional[List[external_group.ExternalGroup]]:
        """
        Gets the groups property value. The groups property
        Returns: Optional[List[external_group.ExternalGroup]]
        """
        return self._groups
    
    @groups.setter
    def groups(self,value: Optional[List[external_group.ExternalGroup]] = None) -> None:
        """
        Sets the groups property value. The groups property
        Args:
            value: Value to set for the groups property.
        """
        self._groups = value
    
    @property
    def ingested_items_count(self,) -> Optional[int]:
        """
        Gets the ingestedItemsCount property value. The number of items ingested into a connection. This value is refreshed every 15 minutes. If the connection state is draft, then ingestedItemsCount will be null.
        Returns: Optional[int]
        """
        return self._ingested_items_count
    
    @ingested_items_count.setter
    def ingested_items_count(self,value: Optional[int] = None) -> None:
        """
        Sets the ingestedItemsCount property value. The number of items ingested into a connection. This value is refreshed every 15 minutes. If the connection state is draft, then ingestedItemsCount will be null.
        Args:
            value: Value to set for the ingestedItemsCount property.
        """
        self._ingested_items_count = value
    
    @property
    def items(self,) -> Optional[List[external_item.ExternalItem]]:
        """
        Gets the items property value. The items property
        Returns: Optional[List[external_item.ExternalItem]]
        """
        return self._items
    
    @items.setter
    def items(self,value: Optional[List[external_item.ExternalItem]] = None) -> None:
        """
        Sets the items property value. The items property
        Args:
            value: Value to set for the items property.
        """
        self._items = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The display name of the connection to be displayed in the Microsoft 365 admin center. Maximum length of 128 characters. Required.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The display name of the connection to be displayed in the Microsoft 365 admin center. Maximum length of 128 characters. Required.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def operations(self,) -> Optional[List[connection_operation.ConnectionOperation]]:
        """
        Gets the operations property value. The operations property
        Returns: Optional[List[connection_operation.ConnectionOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[connection_operation.ConnectionOperation]] = None) -> None:
        """
        Sets the operations property value. The operations property
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def quota(self,) -> Optional[connection_quota.ConnectionQuota]:
        """
        Gets the quota property value. The quota property
        Returns: Optional[connection_quota.ConnectionQuota]
        """
        return self._quota
    
    @quota.setter
    def quota(self,value: Optional[connection_quota.ConnectionQuota] = None) -> None:
        """
        Sets the quota property value. The quota property
        Args:
            value: Value to set for the quota property.
        """
        self._quota = value
    
    @property
    def schema(self,) -> Optional[schema.Schema]:
        """
        Gets the schema property value. The schema property
        Returns: Optional[schema.Schema]
        """
        return self._schema
    
    @schema.setter
    def schema(self,value: Optional[schema.Schema] = None) -> None:
        """
        Sets the schema property value. The schema property
        Args:
            value: Value to set for the schema property.
        """
        self._schema = value
    
    @property
    def search_settings(self,) -> Optional[search_settings.SearchSettings]:
        """
        Gets the searchSettings property value. The settings configuring the search experience for content in this connection, such as the display templates for search results.
        Returns: Optional[search_settings.SearchSettings]
        """
        return self._search_settings
    
    @search_settings.setter
    def search_settings(self,value: Optional[search_settings.SearchSettings] = None) -> None:
        """
        Sets the searchSettings property value. The settings configuring the search experience for content in this connection, such as the display templates for search results.
        Args:
            value: Value to set for the searchSettings property.
        """
        self._search_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("activitySettings", self.activity_settings)
        writer.write_object_value("complianceSettings", self.compliance_settings)
        writer.write_object_value("configuration", self.configuration)
        writer.write_str_value("connectorId", self.connector_id)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("enabledContentExperiences", self.enabled_content_experiences)
        writer.write_collection_of_object_values("groups", self.groups)
        writer.write_int_value("ingestedItemsCount", self.ingested_items_count)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_object_value("quota", self.quota)
        writer.write_object_value("schema", self.schema)
        writer.write_object_value("searchSettings", self.search_settings)
    
    @property
    def state(self,) -> Optional[connection_state.ConnectionState]:
        """
        Gets the state property value. Indicates the current state of the connection. Possible values are draft, ready, obsolete, and limitExceeded. Required.
        Returns: Optional[connection_state.ConnectionState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[connection_state.ConnectionState] = None) -> None:
        """
        Sets the state property value. Indicates the current state of the connection. Possible values are draft, ready, obsolete, and limitExceeded. Required.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

