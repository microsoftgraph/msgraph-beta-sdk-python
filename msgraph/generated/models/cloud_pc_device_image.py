from __future__ import annotations
from datetime import date, datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_device_image_os_status, cloud_pc_device_image_status, cloud_pc_device_image_status_details, entity

from . import entity

class CloudPcDeviceImage(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new CloudPcDeviceImage and sets the default values.
        """
        super().__init__()
        # The display name of the image.
        self._display_name: Optional[str] = None
        # The date the image became unavailable.
        self._expiration_date: Optional[date] = None
        # The data and time that the image was last modified. The time is shown in ISO 8601 format and  Coordinated Universal Time (UTC) time. For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The operating system of the image. For example, Windows 10 Enterprise.
        self._operating_system: Optional[str] = None
        # The OS build version of the image. For example, 1909.
        self._os_build_number: Optional[str] = None
        # The OS status of this image. Possible values are: supported, supportedWithWarning, unknownFutureValue.
        self._os_status: Optional[cloud_pc_device_image_os_status.CloudPcDeviceImageOsStatus] = None
        # The ID of the source image resource on Azure. Required format: /subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/images/{imageName}.
        self._source_image_resource_id: Optional[str] = None
        # The status of the image on Cloud PC. Possible values are: pending, ready, failed.
        self._status: Optional[cloud_pc_device_image_status.CloudPcDeviceImageStatus] = None
        # The details of the status of the image that indicates why the upload failed, if applicable. Possible values are: internalServerError, sourceImageNotFound, osVersionNotSupported, sourceImageInvalid, and sourceImageNotGeneralized.
        self._status_details: Optional[cloud_pc_device_image_status_details.CloudPcDeviceImageStatusDetails] = None
        # The image version. For example, 0.0.1 and 1.5.13.
        self._version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcDeviceImage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcDeviceImage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcDeviceImage()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the image.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the image.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def expiration_date(self,) -> Optional[date]:
        """
        Gets the expirationDate property value. The date the image became unavailable.
        Returns: Optional[date]
        """
        return self._expiration_date
    
    @expiration_date.setter
    def expiration_date(self,value: Optional[date] = None) -> None:
        """
        Sets the expirationDate property value. The date the image became unavailable.
        Args:
            value: Value to set for the expiration_date property.
        """
        self._expiration_date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cloud_pc_device_image_os_status, cloud_pc_device_image_status, cloud_pc_device_image_status_details, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "expirationDate": lambda n : setattr(self, 'expiration_date', n.get_date_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "osBuildNumber": lambda n : setattr(self, 'os_build_number', n.get_str_value()),
            "osStatus": lambda n : setattr(self, 'os_status', n.get_enum_value(cloud_pc_device_image_os_status.CloudPcDeviceImageOsStatus)),
            "sourceImageResourceId": lambda n : setattr(self, 'source_image_resource_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(cloud_pc_device_image_status.CloudPcDeviceImageStatus)),
            "statusDetails": lambda n : setattr(self, 'status_details', n.get_enum_value(cloud_pc_device_image_status_details.CloudPcDeviceImageStatusDetails)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The data and time that the image was last modified. The time is shown in ISO 8601 format and  Coordinated Universal Time (UTC) time. For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The data and time that the image was last modified. The time is shown in ISO 8601 format and  Coordinated Universal Time (UTC) time. For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def operating_system(self,) -> Optional[str]:
        """
        Gets the operatingSystem property value. The operating system of the image. For example, Windows 10 Enterprise.
        Returns: Optional[str]
        """
        return self._operating_system
    
    @operating_system.setter
    def operating_system(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystem property value. The operating system of the image. For example, Windows 10 Enterprise.
        Args:
            value: Value to set for the operating_system property.
        """
        self._operating_system = value
    
    @property
    def os_build_number(self,) -> Optional[str]:
        """
        Gets the osBuildNumber property value. The OS build version of the image. For example, 1909.
        Returns: Optional[str]
        """
        return self._os_build_number
    
    @os_build_number.setter
    def os_build_number(self,value: Optional[str] = None) -> None:
        """
        Sets the osBuildNumber property value. The OS build version of the image. For example, 1909.
        Args:
            value: Value to set for the os_build_number property.
        """
        self._os_build_number = value
    
    @property
    def os_status(self,) -> Optional[cloud_pc_device_image_os_status.CloudPcDeviceImageOsStatus]:
        """
        Gets the osStatus property value. The OS status of this image. Possible values are: supported, supportedWithWarning, unknownFutureValue.
        Returns: Optional[cloud_pc_device_image_os_status.CloudPcDeviceImageOsStatus]
        """
        return self._os_status
    
    @os_status.setter
    def os_status(self,value: Optional[cloud_pc_device_image_os_status.CloudPcDeviceImageOsStatus] = None) -> None:
        """
        Sets the osStatus property value. The OS status of this image. Possible values are: supported, supportedWithWarning, unknownFutureValue.
        Args:
            value: Value to set for the os_status property.
        """
        self._os_status = value
    
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
        writer.write_date_value("expirationDate", self.expiration_date)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_str_value("osBuildNumber", self.os_build_number)
        writer.write_enum_value("osStatus", self.os_status)
        writer.write_str_value("sourceImageResourceId", self.source_image_resource_id)
        writer.write_enum_value("status", self.status)
        writer.write_enum_value("statusDetails", self.status_details)
        writer.write_str_value("version", self.version)
    
    @property
    def source_image_resource_id(self,) -> Optional[str]:
        """
        Gets the sourceImageResourceId property value. The ID of the source image resource on Azure. Required format: /subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/images/{imageName}.
        Returns: Optional[str]
        """
        return self._source_image_resource_id
    
    @source_image_resource_id.setter
    def source_image_resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceImageResourceId property value. The ID of the source image resource on Azure. Required format: /subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/images/{imageName}.
        Args:
            value: Value to set for the source_image_resource_id property.
        """
        self._source_image_resource_id = value
    
    @property
    def status(self,) -> Optional[cloud_pc_device_image_status.CloudPcDeviceImageStatus]:
        """
        Gets the status property value. The status of the image on Cloud PC. Possible values are: pending, ready, failed.
        Returns: Optional[cloud_pc_device_image_status.CloudPcDeviceImageStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[cloud_pc_device_image_status.CloudPcDeviceImageStatus] = None) -> None:
        """
        Sets the status property value. The status of the image on Cloud PC. Possible values are: pending, ready, failed.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def status_details(self,) -> Optional[cloud_pc_device_image_status_details.CloudPcDeviceImageStatusDetails]:
        """
        Gets the statusDetails property value. The details of the status of the image that indicates why the upload failed, if applicable. Possible values are: internalServerError, sourceImageNotFound, osVersionNotSupported, sourceImageInvalid, and sourceImageNotGeneralized.
        Returns: Optional[cloud_pc_device_image_status_details.CloudPcDeviceImageStatusDetails]
        """
        return self._status_details
    
    @status_details.setter
    def status_details(self,value: Optional[cloud_pc_device_image_status_details.CloudPcDeviceImageStatusDetails] = None) -> None:
        """
        Sets the statusDetails property value. The details of the status of the image that indicates why the upload failed, if applicable. Possible values are: internalServerError, sourceImageNotFound, osVersionNotSupported, sourceImageInvalid, and sourceImageNotGeneralized.
        Args:
            value: Value to set for the status_details property.
        """
        self._status_details = value
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. The image version. For example, 0.0.1 and 1.5.13.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. The image version. For example, 0.0.1 and 1.5.13.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

