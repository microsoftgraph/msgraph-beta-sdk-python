from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
usage_right_state = lazy_import('msgraph.generated.models.usage_right_state')

class UsageRight(entity.Entity):
    """
    Casts the previous resource to device.
    """
    @property
    def catalog_id(self,) -> Optional[str]:
        """
        Gets the catalogId property value. Product id corresponding to the usage right.
        Returns: Optional[str]
        """
        return self._catalog_id
    
    @catalog_id.setter
    def catalog_id(self,value: Optional[str] = None) -> None:
        """
        Sets the catalogId property value. Product id corresponding to the usage right.
        Args:
            value: Value to set for the catalogId property.
        """
        self._catalog_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new usageRight and sets the default values.
        """
        super().__init__()
        # Product id corresponding to the usage right.
        self._catalog_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Identifier of the service corresponding to the usage right.
        self._service_identifier: Optional[str] = None
        # The state property
        self._state: Optional[usage_right_state.UsageRightState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UsageRight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UsageRight
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UsageRight()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "catalog_id": lambda n : setattr(self, 'catalog_id', n.get_str_value()),
            "service_identifier": lambda n : setattr(self, 'service_identifier', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(usage_right_state.UsageRightState)),
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
        writer.write_str_value("catalogId", self.catalog_id)
        writer.write_str_value("serviceIdentifier", self.service_identifier)
        writer.write_enum_value("state", self.state)
    
    @property
    def service_identifier(self,) -> Optional[str]:
        """
        Gets the serviceIdentifier property value. Identifier of the service corresponding to the usage right.
        Returns: Optional[str]
        """
        return self._service_identifier
    
    @service_identifier.setter
    def service_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the serviceIdentifier property value. Identifier of the service corresponding to the usage right.
        Args:
            value: Value to set for the serviceIdentifier property.
        """
        self._service_identifier = value
    
    @property
    def state(self,) -> Optional[usage_right_state.UsageRightState]:
        """
        Gets the state property value. The state property
        Returns: Optional[usage_right_state.UsageRightState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[usage_right_state.UsageRightState] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

