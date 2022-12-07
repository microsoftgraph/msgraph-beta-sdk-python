from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

application = lazy_import('msgraph.generated.models.application')
connector = lazy_import('msgraph.generated.models.connector')
connector_group_region = lazy_import('msgraph.generated.models.connector_group_region')
connector_group_type = lazy_import('msgraph.generated.models.connector_group_type')
entity = lazy_import('msgraph.generated.models.entity')

class ConnectorGroup(entity.Entity):
    @property
    def applications(self,) -> Optional[List[application.Application]]:
        """
        Gets the applications property value. The applications property
        Returns: Optional[List[application.Application]]
        """
        return self._applications
    
    @applications.setter
    def applications(self,value: Optional[List[application.Application]] = None) -> None:
        """
        Sets the applications property value. The applications property
        Args:
            value: Value to set for the applications property.
        """
        self._applications = value
    
    @property
    def connector_group_type(self,) -> Optional[connector_group_type.ConnectorGroupType]:
        """
        Gets the connectorGroupType property value. The connectorGroupType property
        Returns: Optional[connector_group_type.ConnectorGroupType]
        """
        return self._connector_group_type
    
    @connector_group_type.setter
    def connector_group_type(self,value: Optional[connector_group_type.ConnectorGroupType] = None) -> None:
        """
        Sets the connectorGroupType property value. The connectorGroupType property
        Args:
            value: Value to set for the connectorGroupType property.
        """
        self._connector_group_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new connectorGroup and sets the default values.
        """
        super().__init__()
        # The applications property
        self._applications: Optional[List[application.Application]] = None
        # The connectorGroupType property
        self._connector_group_type: Optional[connector_group_type.ConnectorGroupType] = None
        # Indicates if the connectorGroup is the default connectorGroup. Only a single connector group can be the default connectorGroup and this is pre-set by the system. Read-only.
        self._is_default: Optional[bool] = None
        # The members property
        self._members: Optional[List[connector.Connector]] = None
        # The name associated with the connectorGroup.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The region the connectorGroup is assigned to and will optimize traffic for. This region can only be set if no connectors or applications are assigned to the connectorGroup. The possible values are: nam (for North America), eur (for Europe), aus (for Australia), asia (for Asia), ind (for India), and unknownFutureValue.
        self._region: Optional[connector_group_region.ConnectorGroupRegion] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConnectorGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConnectorGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConnectorGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "applications": lambda n : setattr(self, 'applications', n.get_collection_of_object_values(application.Application)),
            "connector_group_type": lambda n : setattr(self, 'connector_group_type', n.get_enum_value(connector_group_type.ConnectorGroupType)),
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(connector.Connector)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_enum_value(connector_group_region.ConnectorGroupRegion)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_default(self,) -> Optional[bool]:
        """
        Gets the isDefault property value. Indicates if the connectorGroup is the default connectorGroup. Only a single connector group can be the default connectorGroup and this is pre-set by the system. Read-only.
        Returns: Optional[bool]
        """
        return self._is_default
    
    @is_default.setter
    def is_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefault property value. Indicates if the connectorGroup is the default connectorGroup. Only a single connector group can be the default connectorGroup and this is pre-set by the system. Read-only.
        Args:
            value: Value to set for the isDefault property.
        """
        self._is_default = value
    
    @property
    def members(self,) -> Optional[List[connector.Connector]]:
        """
        Gets the members property value. The members property
        Returns: Optional[List[connector.Connector]]
        """
        return self._members
    
    @members.setter
    def members(self,value: Optional[List[connector.Connector]] = None) -> None:
        """
        Sets the members property value. The members property
        Args:
            value: Value to set for the members property.
        """
        self._members = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name associated with the connectorGroup.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name associated with the connectorGroup.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def region(self,) -> Optional[connector_group_region.ConnectorGroupRegion]:
        """
        Gets the region property value. The region the connectorGroup is assigned to and will optimize traffic for. This region can only be set if no connectors or applications are assigned to the connectorGroup. The possible values are: nam (for North America), eur (for Europe), aus (for Australia), asia (for Asia), ind (for India), and unknownFutureValue.
        Returns: Optional[connector_group_region.ConnectorGroupRegion]
        """
        return self._region
    
    @region.setter
    def region(self,value: Optional[connector_group_region.ConnectorGroupRegion] = None) -> None:
        """
        Sets the region property value. The region the connectorGroup is assigned to and will optimize traffic for. This region can only be set if no connectors or applications are assigned to the connectorGroup. The possible values are: nam (for North America), eur (for Europe), aus (for Australia), asia (for Asia), ind (for India), and unknownFutureValue.
        Args:
            value: Value to set for the region property.
        """
        self._region = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("applications", self.applications)
        writer.write_enum_value("connectorGroupType", self.connector_group_type)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("region", self.region)
    

