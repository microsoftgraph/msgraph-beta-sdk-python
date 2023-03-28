from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import bitlocker_recovery_key, entity

from . import entity

class Bitlocker(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new bitlocker and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The recovery keys associated with the bitlocker entity.
        self._recovery_keys: Optional[List[bitlocker_recovery_key.BitlockerRecoveryKey]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Bitlocker:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Bitlocker
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Bitlocker()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import bitlocker_recovery_key, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "recoveryKeys": lambda n : setattr(self, 'recovery_keys', n.get_collection_of_object_values(bitlocker_recovery_key.BitlockerRecoveryKey)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def recovery_keys(self,) -> Optional[List[bitlocker_recovery_key.BitlockerRecoveryKey]]:
        """
        Gets the recoveryKeys property value. The recovery keys associated with the bitlocker entity.
        Returns: Optional[List[bitlocker_recovery_key.BitlockerRecoveryKey]]
        """
        return self._recovery_keys
    
    @recovery_keys.setter
    def recovery_keys(self,value: Optional[List[bitlocker_recovery_key.BitlockerRecoveryKey]] = None) -> None:
        """
        Sets the recoveryKeys property value. The recovery keys associated with the bitlocker entity.
        Args:
            value: Value to set for the recovery_keys property.
        """
        self._recovery_keys = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("recoveryKeys", self.recovery_keys)
    

