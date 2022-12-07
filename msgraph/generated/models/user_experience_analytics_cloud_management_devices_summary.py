from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class UserExperienceAnalyticsCloudManagementDevicesSummary(AdditionalDataHolder, Parsable):
    """
    The user experience work from anywhere Cloud management devices summary.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def co_managed_device_count(self,) -> Optional[int]:
        """
        Gets the coManagedDeviceCount property value. Total number of  co-managed devices.
        Returns: Optional[int]
        """
        return self._co_managed_device_count
    
    @co_managed_device_count.setter
    def co_managed_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the coManagedDeviceCount property value. Total number of  co-managed devices.
        Args:
            value: Value to set for the coManagedDeviceCount property.
        """
        self._co_managed_device_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsCloudManagementDevicesSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Total number of  co-managed devices.
        self._co_managed_device_count: Optional[int] = None
        # The count of intune devices that are not autopilot registerd.
        self._intune_device_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Total count of tenant attach devices.
        self._tenant_attach_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsCloudManagementDevicesSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsCloudManagementDevicesSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsCloudManagementDevicesSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "co_managed_device_count": lambda n : setattr(self, 'co_managed_device_count', n.get_int_value()),
            "intune_device_count": lambda n : setattr(self, 'intune_device_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tenant_attach_device_count": lambda n : setattr(self, 'tenant_attach_device_count', n.get_int_value()),
        }
        return fields
    
    @property
    def intune_device_count(self,) -> Optional[int]:
        """
        Gets the intuneDeviceCount property value. The count of intune devices that are not autopilot registerd.
        Returns: Optional[int]
        """
        return self._intune_device_count
    
    @intune_device_count.setter
    def intune_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the intuneDeviceCount property value. The count of intune devices that are not autopilot registerd.
        Args:
            value: Value to set for the intuneDeviceCount property.
        """
        self._intune_device_count = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("coManagedDeviceCount", self.co_managed_device_count)
        writer.write_int_value("intuneDeviceCount", self.intune_device_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("tenantAttachDeviceCount", self.tenant_attach_device_count)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def tenant_attach_device_count(self,) -> Optional[int]:
        """
        Gets the tenantAttachDeviceCount property value. Total count of tenant attach devices.
        Returns: Optional[int]
        """
        return self._tenant_attach_device_count
    
    @tenant_attach_device_count.setter
    def tenant_attach_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the tenantAttachDeviceCount property value. Total count of tenant attach devices.
        Args:
            value: Value to set for the tenantAttachDeviceCount property.
        """
        self._tenant_attach_device_count = value
    

