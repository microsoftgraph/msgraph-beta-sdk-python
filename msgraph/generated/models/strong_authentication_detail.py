from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class StrongAuthenticationDetail(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new StrongAuthenticationDetail and sets the default values.
        """
        super().__init__()
        # The encryptedPinHashHistory property
        self._encrypted_pin_hash_history: Optional[bytes] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The proofupTime property
        self._proofup_time: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> StrongAuthenticationDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: StrongAuthenticationDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return StrongAuthenticationDetail()
    
    @property
    def encrypted_pin_hash_history(self,) -> Optional[bytes]:
        """
        Gets the encryptedPinHashHistory property value. The encryptedPinHashHistory property
        Returns: Optional[bytes]
        """
        return self._encrypted_pin_hash_history
    
    @encrypted_pin_hash_history.setter
    def encrypted_pin_hash_history(self,value: Optional[bytes] = None) -> None:
        """
        Sets the encryptedPinHashHistory property value. The encryptedPinHashHistory property
        Args:
            value: Value to set for the encryptedPinHashHistory property.
        """
        self._encrypted_pin_hash_history = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "encrypted_pin_hash_history": lambda n : setattr(self, 'encrypted_pin_hash_history', n.get_bytes_value()),
            "proofup_time": lambda n : setattr(self, 'proofup_time', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def proofup_time(self,) -> Optional[int]:
        """
        Gets the proofupTime property value. The proofupTime property
        Returns: Optional[int]
        """
        return self._proofup_time
    
    @proofup_time.setter
    def proofup_time(self,value: Optional[int] = None) -> None:
        """
        Sets the proofupTime property value. The proofupTime property
        Args:
            value: Value to set for the proofupTime property.
        """
        self._proofup_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("encryptedPinHashHistory", self.encrypted_pin_hash_history)
        writer.write_int_value("proofupTime", self.proofup_time)
    

