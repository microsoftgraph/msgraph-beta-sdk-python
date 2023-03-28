from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import updatable_asset, updatable_asset_enrollment, updatable_asset_error

from . import updatable_asset

class AzureADDevice(updatable_asset.UpdatableAsset):
    def __init__(self,) -> None:
        """
        Instantiates a new AzureADDevice and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.azureADDevice"
        # Specifies areas of the service in which the device is enrolled. Read-only. Returned by default.
        self._enrollments: Optional[List[updatable_asset_enrollment.UpdatableAssetEnrollment]] = None
        # Specifies any errors that prevent the device from being enrolled in update management or receving deployed content. Read-only. Returned by default.
        self._errors: Optional[List[updatable_asset_error.UpdatableAssetError]] = None
    
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
    
    @property
    def enrollments(self,) -> Optional[List[updatable_asset_enrollment.UpdatableAssetEnrollment]]:
        """
        Gets the enrollments property value. Specifies areas of the service in which the device is enrolled. Read-only. Returned by default.
        Returns: Optional[List[updatable_asset_enrollment.UpdatableAssetEnrollment]]
        """
        return self._enrollments
    
    @enrollments.setter
    def enrollments(self,value: Optional[List[updatable_asset_enrollment.UpdatableAssetEnrollment]] = None) -> None:
        """
        Sets the enrollments property value. Specifies areas of the service in which the device is enrolled. Read-only. Returned by default.
        Args:
            value: Value to set for the enrollments property.
        """
        self._enrollments = value
    
    @property
    def errors(self,) -> Optional[List[updatable_asset_error.UpdatableAssetError]]:
        """
        Gets the errors property value. Specifies any errors that prevent the device from being enrolled in update management or receving deployed content. Read-only. Returned by default.
        Returns: Optional[List[updatable_asset_error.UpdatableAssetError]]
        """
        return self._errors
    
    @errors.setter
    def errors(self,value: Optional[List[updatable_asset_error.UpdatableAssetError]] = None) -> None:
        """
        Sets the errors property value. Specifies any errors that prevent the device from being enrolled in update management or receving deployed content. Read-only. Returned by default.
        Args:
            value: Value to set for the errors property.
        """
        self._errors = value
    
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
    

