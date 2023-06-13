from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import updatable_asset, updatable_asset_enrollment, updatable_asset_error

from . import updatable_asset

@dataclass
class AzureADDevice(updatable_asset.UpdatableAsset):
    odata_type = "#microsoft.graph.windowsUpdates.azureADDevice"
    # Specifies areas of the service in which the device is enrolled. Read-only. Returned by default.
    enrollments: Optional[List[updatable_asset_enrollment.UpdatableAssetEnrollment]] = None
    # Specifies any errors that prevent the device from being enrolled in update management or receving deployed content. Read-only. Returned by default.
    errors: Optional[List[updatable_asset_error.UpdatableAssetError]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AzureADDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AzureADDevice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AzureADDevice()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import updatable_asset, updatable_asset_enrollment, updatable_asset_error

        fields: Dict[str, Callable[[Any], None]] = {
            "enrollments": lambda n : setattr(self, 'enrollments', n.get_collection_of_object_values(updatable_asset_enrollment.UpdatableAssetEnrollment)),
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(updatable_asset_error.UpdatableAssetError)),
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
        writer.write_collection_of_object_values("enrollments", self.enrollments)
        writer.write_collection_of_object_values("errors", self.errors)
    

