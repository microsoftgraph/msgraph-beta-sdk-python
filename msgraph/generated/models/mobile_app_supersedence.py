from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_app_relationship = lazy_import('msgraph.generated.models.mobile_app_relationship')
mobile_app_supersedence_type = lazy_import('msgraph.generated.models.mobile_app_supersedence_type')

class MobileAppSupersedence(mobile_app_relationship.MobileAppRelationship):
    def __init__(self,) -> None:
        """
        Instantiates a new MobileAppSupersedence and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.mobileAppSupersedence"
        # The total number of apps directly or indirectly superseded by the child app.
        self._superseded_app_count: Optional[int] = None
        # Indicates the supersedence type associated with a relationship between two mobile apps.
        self._supersedence_type: Optional[mobile_app_supersedence_type.MobileAppSupersedenceType] = None
        # The total number of apps directly or indirectly superseding the parent app.
        self._superseding_app_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppSupersedence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppSupersedence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppSupersedence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "superseded_app_count": lambda n : setattr(self, 'superseded_app_count', n.get_int_value()),
            "supersedence_type": lambda n : setattr(self, 'supersedence_type', n.get_enum_value(mobile_app_supersedence_type.MobileAppSupersedenceType)),
            "superseding_app_count": lambda n : setattr(self, 'superseding_app_count', n.get_int_value()),
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
        writer.write_int_value("supersededAppCount", self.superseded_app_count)
        writer.write_enum_value("supersedenceType", self.supersedence_type)
        writer.write_int_value("supersedingAppCount", self.superseding_app_count)
    
    @property
    def superseded_app_count(self,) -> Optional[int]:
        """
        Gets the supersededAppCount property value. The total number of apps directly or indirectly superseded by the child app.
        Returns: Optional[int]
        """
        return self._superseded_app_count
    
    @superseded_app_count.setter
    def superseded_app_count(self,value: Optional[int] = None) -> None:
        """
        Sets the supersededAppCount property value. The total number of apps directly or indirectly superseded by the child app.
        Args:
            value: Value to set for the supersededAppCount property.
        """
        self._superseded_app_count = value
    
    @property
    def supersedence_type(self,) -> Optional[mobile_app_supersedence_type.MobileAppSupersedenceType]:
        """
        Gets the supersedenceType property value. Indicates the supersedence type associated with a relationship between two mobile apps.
        Returns: Optional[mobile_app_supersedence_type.MobileAppSupersedenceType]
        """
        return self._supersedence_type
    
    @supersedence_type.setter
    def supersedence_type(self,value: Optional[mobile_app_supersedence_type.MobileAppSupersedenceType] = None) -> None:
        """
        Sets the supersedenceType property value. Indicates the supersedence type associated with a relationship between two mobile apps.
        Args:
            value: Value to set for the supersedenceType property.
        """
        self._supersedence_type = value
    
    @property
    def superseding_app_count(self,) -> Optional[int]:
        """
        Gets the supersedingAppCount property value. The total number of apps directly or indirectly superseding the parent app.
        Returns: Optional[int]
        """
        return self._superseding_app_count
    
    @superseding_app_count.setter
    def superseding_app_count(self,value: Optional[int] = None) -> None:
        """
        Sets the supersedingAppCount property value. The total number of apps directly or indirectly superseding the parent app.
        Args:
            value: Value to set for the supersedingAppCount property.
        """
        self._superseding_app_count = value
    

