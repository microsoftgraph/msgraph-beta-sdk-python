from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class OemWarrantyInformationOnboarding(entity.Entity):
    """
    Warranty status entity for a given OEM
    """
    @property
    def available(self,) -> Optional[bool]:
        """
        Gets the available property value. Specifies whether warranty API is available. This property is read-only.
        Returns: Optional[bool]
        """
        return self._available
    
    @available.setter
    def available(self,value: Optional[bool] = None) -> None:
        """
        Sets the available property value. Specifies whether warranty API is available. This property is read-only.
        Args:
            value: Value to set for the available property.
        """
        self._available = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new oemWarrantyInformationOnboarding and sets the default values.
        """
        super().__init__()
        # Specifies whether warranty API is available. This property is read-only.
        self._available: Optional[bool] = None
        # Specifies whether warranty query is enabled for given OEM. This property is read-only.
        self._enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # OEM name. This property is read-only.
        self._oem_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OemWarrantyInformationOnboarding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OemWarrantyInformationOnboarding
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OemWarrantyInformationOnboarding()
    
    @property
    def enabled(self,) -> Optional[bool]:
        """
        Gets the enabled property value. Specifies whether warranty query is enabled for given OEM. This property is read-only.
        Returns: Optional[bool]
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the enabled property value. Specifies whether warranty query is enabled for given OEM. This property is read-only.
        Args:
            value: Value to set for the enabled property.
        """
        self._enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "available": lambda n : setattr(self, 'available', n.get_bool_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "oem_name": lambda n : setattr(self, 'oem_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def oem_name(self,) -> Optional[str]:
        """
        Gets the oemName property value. OEM name. This property is read-only.
        Returns: Optional[str]
        """
        return self._oem_name
    
    @oem_name.setter
    def oem_name(self,value: Optional[str] = None) -> None:
        """
        Sets the oemName property value. OEM name. This property is read-only.
        Args:
            value: Value to set for the oemName property.
        """
        self._oem_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
    

