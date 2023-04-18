from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class CloudPcSharedUseServicePlan(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new CloudPcSharedUseServicePlan and sets the default values.
        """
        super().__init__()
        # The display name of the shared-use service plan.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Total number of shared-use service plans purchased by the customer.
        self._total_count: Optional[int] = None
        # The number of service plans that the account uses.
        self._used_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcSharedUseServicePlan:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcSharedUseServicePlan
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcSharedUseServicePlan()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the shared-use service plan.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the shared-use service plan.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "totalCount": lambda n : setattr(self, 'total_count', n.get_int_value()),
            "usedCount": lambda n : setattr(self, 'used_count', n.get_int_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("totalCount", self.total_count)
        writer.write_int_value("usedCount", self.used_count)
    
    @property
    def total_count(self,) -> Optional[int]:
        """
        Gets the totalCount property value. Total number of shared-use service plans purchased by the customer.
        Returns: Optional[int]
        """
        return self._total_count
    
    @total_count.setter
    def total_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalCount property value. Total number of shared-use service plans purchased by the customer.
        Args:
            value: Value to set for the total_count property.
        """
        self._total_count = value
    
    @property
    def used_count(self,) -> Optional[int]:
        """
        Gets the usedCount property value. The number of service plans that the account uses.
        Returns: Optional[int]
        """
        return self._used_count
    
    @used_count.setter
    def used_count(self,value: Optional[int] = None) -> None:
        """
        Sets the usedCount property value. The number of service plans that the account uses.
        Args:
            value: Value to set for the used_count property.
        """
        self._used_count = value
    

