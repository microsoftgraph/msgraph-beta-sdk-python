from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_device_image_error_code import CloudPcDeviceImageErrorCode
    from .cloud_pc_device_image_os_status import CloudPcDeviceImageOsStatus
    from .cloud_pc_device_image_status import CloudPcDeviceImageStatus
    from .cloud_pc_device_image_status_details import CloudPcDeviceImageStatusDetails
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcDeviceImage(Entity, Parsable):
    # The display name of the associated device image. The device image display name and the version are used to uniquely identify the Cloud PC device image. Read-only.
    display_name: Optional[str] = None
    # The error code of the status of the image that indicates why the upload failed, if applicable. Possible values are: internalServerError, sourceImageNotFound, osVersionNotSupported, sourceImageInvalid, sourceImageNotGeneralized, unknownFutureValue, vmAlreadyAzureAdJoined, paidSourceImageNotSupport, sourceImageNotSupportCustomizeVMName, sourceImageSizeExceedsLimitation. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: vmAlreadyAzureAdJoined, paidSourceImageNotSupport, sourceImageNotSupportCustomizeVMName, sourceImageSizeExceedsLimitation. Read-only.
    error_code: Optional[CloudPcDeviceImageErrorCode] = None
    # The date when the image became unavailable. Read-only.
    expiration_date: Optional[datetime.date] = None
    # The data and time when the image was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operating system of the image. For example, Windows 10 Enterprise. Read-only.
    operating_system: Optional[str] = None
    # The OS build version of the image. For example, 1909. Read-only.
    os_build_number: Optional[str] = None
    # The OS status of this image. Possible values are: supported, supportedWithWarning, unknown, unknownFutureValue. The default value is unknown. Read-only.
    os_status: Optional[CloudPcDeviceImageOsStatus] = None
    # The operating system version of this image. For example, 10.0.22000.296. Read-only.
    os_version_number: Optional[str] = None
    # The scopeIds property
    scope_ids: Optional[List[str]] = None
    # The unique identifier (ID) of the source image resource on Azure. The required ID format is: '/subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/images/{imageName}'. Read-only.
    source_image_resource_id: Optional[str] = None
    # The status of the image on the Cloud PC. Possible values are: pending, ready, failed, unknownFutureValue. Read-only.
    status: Optional[CloudPcDeviceImageStatus] = None
    # The details of the status of the image that indicates why the upload failed, if applicable. Possible values are: internalServerError, sourceImageNotFound, osVersionNotSupported, sourceImageInvalid, sourceImageNotGeneralized, unknownFutureValue, vmAlreadyAzureAdJoined, paidSourceImageNotSupport, sourceImageNotSupportCustomizeVMName, sourceImageSizeExceedsLimitation. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: vmAlreadyAzureAdJoined, paidSourceImageNotSupport, sourceImageNotSupportCustomizeVMName, sourceImageSizeExceedsLimitation. Read-only. The statusDetails property is deprecated and will stop returning data on January 31, 2024. Going forward, use the errorCode property.
    status_details: Optional[CloudPcDeviceImageStatusDetails] = None
    # The image version. For example, 0.0.1 and 1.5.13. Read-only.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcDeviceImage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcDeviceImage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcDeviceImage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_device_image_error_code import CloudPcDeviceImageErrorCode
        from .cloud_pc_device_image_os_status import CloudPcDeviceImageOsStatus
        from .cloud_pc_device_image_status import CloudPcDeviceImageStatus
        from .cloud_pc_device_image_status_details import CloudPcDeviceImageStatusDetails
        from .entity import Entity

        from .cloud_pc_device_image_error_code import CloudPcDeviceImageErrorCode
        from .cloud_pc_device_image_os_status import CloudPcDeviceImageOsStatus
        from .cloud_pc_device_image_status import CloudPcDeviceImageStatus
        from .cloud_pc_device_image_status_details import CloudPcDeviceImageStatusDetails
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_enum_value(CloudPcDeviceImageErrorCode)),
            "expirationDate": lambda n : setattr(self, 'expiration_date', n.get_date_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "osBuildNumber": lambda n : setattr(self, 'os_build_number', n.get_str_value()),
            "osStatus": lambda n : setattr(self, 'os_status', n.get_enum_value(CloudPcDeviceImageOsStatus)),
            "osVersionNumber": lambda n : setattr(self, 'os_version_number', n.get_str_value()),
            "scopeIds": lambda n : setattr(self, 'scope_ids', n.get_collection_of_primitive_values(str)),
            "sourceImageResourceId": lambda n : setattr(self, 'source_image_resource_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CloudPcDeviceImageStatus)),
            "statusDetails": lambda n : setattr(self, 'status_details', n.get_enum_value(CloudPcDeviceImageStatusDetails)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .cloud_pc_device_image_error_code import CloudPcDeviceImageErrorCode
        from .cloud_pc_device_image_os_status import CloudPcDeviceImageOsStatus
        from .cloud_pc_device_image_status import CloudPcDeviceImageStatus
        from .cloud_pc_device_image_status_details import CloudPcDeviceImageStatusDetails
        from .entity import Entity

        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("errorCode", self.error_code)
        writer.write_date_value("expirationDate", self.expiration_date)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_str_value("osBuildNumber", self.os_build_number)
        writer.write_enum_value("osStatus", self.os_status)
        writer.write_str_value("osVersionNumber", self.os_version_number)
        writer.write_collection_of_primitive_values("scopeIds", self.scope_ids)
        writer.write_str_value("sourceImageResourceId", self.source_image_resource_id)
        writer.write_enum_value("status", self.status)
        writer.write_enum_value("statusDetails", self.status_details)
        writer.write_str_value("version", self.version)
    

