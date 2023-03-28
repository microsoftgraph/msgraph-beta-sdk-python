from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_enrollment_configuration, device_enrollment_platform_restriction

from . import device_enrollment_configuration

class DeviceEnrollmentPlatformRestrictionsConfiguration(device_enrollment_configuration.DeviceEnrollmentConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceEnrollmentPlatformRestrictionsConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceEnrollmentPlatformRestrictionsConfiguration"
        # Android for work restrictions based on platform, platform operating system version, and device ownership
        self._android_for_work_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
        # Android restrictions based on platform, platform operating system version, and device ownership
        self._android_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
        # Ios restrictions based on platform, platform operating system version, and device ownership
        self._ios_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
        # Mac restrictions based on platform, platform operating system version, and device ownership
        self._mac_o_s_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
        # Mac restrictions based on platform, platform operating system version, and device ownership
        self._mac_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
        # Windows Home Sku restrictions based on platform, platform operating system version, and device ownership
        self._windows_home_sku_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
        # Windows mobile restrictions based on platform, platform operating system version, and device ownership
        self._windows_mobile_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
        # Windows restrictions based on platform, platform operating system version, and device ownership
        self._windows_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
    
    @property
    def android_for_work_restriction(self,) -> Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]:
        """
        Gets the androidForWorkRestriction property value. Android for work restrictions based on platform, platform operating system version, and device ownership
        Returns: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]
        """
        return self._android_for_work_restriction
    
    @android_for_work_restriction.setter
    def android_for_work_restriction(self,value: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None) -> None:
        """
        Sets the androidForWorkRestriction property value. Android for work restrictions based on platform, platform operating system version, and device ownership
        Args:
            value: Value to set for the android_for_work_restriction property.
        """
        self._android_for_work_restriction = value
    
    @property
    def android_restriction(self,) -> Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]:
        """
        Gets the androidRestriction property value. Android restrictions based on platform, platform operating system version, and device ownership
        Returns: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]
        """
        return self._android_restriction
    
    @android_restriction.setter
    def android_restriction(self,value: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None) -> None:
        """
        Sets the androidRestriction property value. Android restrictions based on platform, platform operating system version, and device ownership
        Args:
            value: Value to set for the android_restriction property.
        """
        self._android_restriction = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceEnrollmentPlatformRestrictionsConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEnrollmentPlatformRestrictionsConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceEnrollmentPlatformRestrictionsConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_enrollment_configuration, device_enrollment_platform_restriction

        fields: Dict[str, Callable[[Any], None]] = {
            "androidForWorkRestriction": lambda n : setattr(self, 'android_for_work_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
            "androidRestriction": lambda n : setattr(self, 'android_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
            "iosRestriction": lambda n : setattr(self, 'ios_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
            "macOSRestriction": lambda n : setattr(self, 'mac_o_s_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
            "macRestriction": lambda n : setattr(self, 'mac_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
            "windowsHomeSkuRestriction": lambda n : setattr(self, 'windows_home_sku_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
            "windowsMobileRestriction": lambda n : setattr(self, 'windows_mobile_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
            "windowsRestriction": lambda n : setattr(self, 'windows_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ios_restriction(self,) -> Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]:
        """
        Gets the iosRestriction property value. Ios restrictions based on platform, platform operating system version, and device ownership
        Returns: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]
        """
        return self._ios_restriction
    
    @ios_restriction.setter
    def ios_restriction(self,value: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None) -> None:
        """
        Sets the iosRestriction property value. Ios restrictions based on platform, platform operating system version, and device ownership
        Args:
            value: Value to set for the ios_restriction property.
        """
        self._ios_restriction = value
    
    @property
    def mac_o_s_restriction(self,) -> Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]:
        """
        Gets the macOSRestriction property value. Mac restrictions based on platform, platform operating system version, and device ownership
        Returns: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]
        """
        return self._mac_o_s_restriction
    
    @mac_o_s_restriction.setter
    def mac_o_s_restriction(self,value: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None) -> None:
        """
        Sets the macOSRestriction property value. Mac restrictions based on platform, platform operating system version, and device ownership
        Args:
            value: Value to set for the mac_o_s_restriction property.
        """
        self._mac_o_s_restriction = value
    
    @property
    def mac_restriction(self,) -> Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]:
        """
        Gets the macRestriction property value. Mac restrictions based on platform, platform operating system version, and device ownership
        Returns: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]
        """
        return self._mac_restriction
    
    @mac_restriction.setter
    def mac_restriction(self,value: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None) -> None:
        """
        Sets the macRestriction property value. Mac restrictions based on platform, platform operating system version, and device ownership
        Args:
            value: Value to set for the mac_restriction property.
        """
        self._mac_restriction = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("androidForWorkRestriction", self.android_for_work_restriction)
        writer.write_object_value("androidRestriction", self.android_restriction)
        writer.write_object_value("iosRestriction", self.ios_restriction)
        writer.write_object_value("macOSRestriction", self.mac_o_s_restriction)
        writer.write_object_value("macRestriction", self.mac_restriction)
        writer.write_object_value("windowsHomeSkuRestriction", self.windows_home_sku_restriction)
        writer.write_object_value("windowsMobileRestriction", self.windows_mobile_restriction)
        writer.write_object_value("windowsRestriction", self.windows_restriction)
    
    @property
    def windows_home_sku_restriction(self,) -> Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]:
        """
        Gets the windowsHomeSkuRestriction property value. Windows Home Sku restrictions based on platform, platform operating system version, and device ownership
        Returns: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]
        """
        return self._windows_home_sku_restriction
    
    @windows_home_sku_restriction.setter
    def windows_home_sku_restriction(self,value: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None) -> None:
        """
        Sets the windowsHomeSkuRestriction property value. Windows Home Sku restrictions based on platform, platform operating system version, and device ownership
        Args:
            value: Value to set for the windows_home_sku_restriction property.
        """
        self._windows_home_sku_restriction = value
    
    @property
    def windows_mobile_restriction(self,) -> Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]:
        """
        Gets the windowsMobileRestriction property value. Windows mobile restrictions based on platform, platform operating system version, and device ownership
        Returns: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]
        """
        return self._windows_mobile_restriction
    
    @windows_mobile_restriction.setter
    def windows_mobile_restriction(self,value: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None) -> None:
        """
        Sets the windowsMobileRestriction property value. Windows mobile restrictions based on platform, platform operating system version, and device ownership
        Args:
            value: Value to set for the windows_mobile_restriction property.
        """
        self._windows_mobile_restriction = value
    
    @property
    def windows_restriction(self,) -> Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]:
        """
        Gets the windowsRestriction property value. Windows restrictions based on platform, platform operating system version, and device ownership
        Returns: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]
        """
        return self._windows_restriction
    
    @windows_restriction.setter
    def windows_restriction(self,value: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None) -> None:
        """
        Sets the windowsRestriction property value. Windows restrictions based on platform, platform operating system version, and device ownership
        Args:
            value: Value to set for the windows_restriction property.
        """
        self._windows_restriction = value
    

