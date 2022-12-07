from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

imported_apple_device_identity = lazy_import('msgraph.generated.models.imported_apple_device_identity')

class ImportedAppleDeviceIdentityResult(imported_apple_device_identity.ImportedAppleDeviceIdentity):
    def __init__(self,) -> None:
        """
        Instantiates a new ImportedAppleDeviceIdentityResult and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Status of imported device identity
        self._status: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ImportedAppleDeviceIdentityResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ImportedAppleDeviceIdentityResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ImportedAppleDeviceIdentityResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "status": lambda n : setattr(self, 'status', n.get_bool_value()),
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
        writer.write_bool_value("status", self.status)
    
    @property
    def status(self,) -> Optional[bool]:
        """
        Gets the status property value. Status of imported device identity
        Returns: Optional[bool]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[bool] = None) -> None:
        """
        Sets the status property value. Status of imported device identity
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

