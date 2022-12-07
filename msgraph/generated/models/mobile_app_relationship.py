from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
mobile_app_relationship_type = lazy_import('msgraph.generated.models.mobile_app_relationship_type')

class MobileAppRelationship(entity.Entity):
    """
    Describes a relationship between two mobile apps.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new mobileAppRelationship and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The target mobile app's display name.
        self._target_display_name: Optional[str] = None
        # The target mobile app's display version.
        self._target_display_version: Optional[str] = None
        # The target mobile app's app id.
        self._target_id: Optional[str] = None
        # The target mobile app's publisher.
        self._target_publisher: Optional[str] = None
        # Indicates whether the target of a relationship is the parent or the child in the relationship.
        self._target_type: Optional[mobile_app_relationship_type.MobileAppRelationshipType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppRelationship:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppRelationship
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppRelationship()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "target_display_name": lambda n : setattr(self, 'target_display_name', n.get_str_value()),
            "target_display_version": lambda n : setattr(self, 'target_display_version', n.get_str_value()),
            "target_id": lambda n : setattr(self, 'target_id', n.get_str_value()),
            "target_publisher": lambda n : setattr(self, 'target_publisher', n.get_str_value()),
            "target_type": lambda n : setattr(self, 'target_type', n.get_enum_value(mobile_app_relationship_type.MobileAppRelationshipType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("targetDisplayName", self.target_display_name)
        writer.write_str_value("targetDisplayVersion", self.target_display_version)
        writer.write_str_value("targetId", self.target_id)
        writer.write_str_value("targetPublisher", self.target_publisher)
        writer.write_enum_value("targetType", self.target_type)
    
    @property
    def target_display_name(self,) -> Optional[str]:
        """
        Gets the targetDisplayName property value. The target mobile app's display name.
        Returns: Optional[str]
        """
        return self._target_display_name
    
    @target_display_name.setter
    def target_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the targetDisplayName property value. The target mobile app's display name.
        Args:
            value: Value to set for the targetDisplayName property.
        """
        self._target_display_name = value
    
    @property
    def target_display_version(self,) -> Optional[str]:
        """
        Gets the targetDisplayVersion property value. The target mobile app's display version.
        Returns: Optional[str]
        """
        return self._target_display_version
    
    @target_display_version.setter
    def target_display_version(self,value: Optional[str] = None) -> None:
        """
        Sets the targetDisplayVersion property value. The target mobile app's display version.
        Args:
            value: Value to set for the targetDisplayVersion property.
        """
        self._target_display_version = value
    
    @property
    def target_id(self,) -> Optional[str]:
        """
        Gets the targetId property value. The target mobile app's app id.
        Returns: Optional[str]
        """
        return self._target_id
    
    @target_id.setter
    def target_id(self,value: Optional[str] = None) -> None:
        """
        Sets the targetId property value. The target mobile app's app id.
        Args:
            value: Value to set for the targetId property.
        """
        self._target_id = value
    
    @property
    def target_publisher(self,) -> Optional[str]:
        """
        Gets the targetPublisher property value. The target mobile app's publisher.
        Returns: Optional[str]
        """
        return self._target_publisher
    
    @target_publisher.setter
    def target_publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the targetPublisher property value. The target mobile app's publisher.
        Args:
            value: Value to set for the targetPublisher property.
        """
        self._target_publisher = value
    
    @property
    def target_type(self,) -> Optional[mobile_app_relationship_type.MobileAppRelationshipType]:
        """
        Gets the targetType property value. Indicates whether the target of a relationship is the parent or the child in the relationship.
        Returns: Optional[mobile_app_relationship_type.MobileAppRelationshipType]
        """
        return self._target_type
    
    @target_type.setter
    def target_type(self,value: Optional[mobile_app_relationship_type.MobileAppRelationshipType] = None) -> None:
        """
        Sets the targetType property value. Indicates whether the target of a relationship is the parent or the child in the relationship.
        Args:
            value: Value to set for the targetType property.
        """
        self._target_type = value
    

