from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class UserExperienceAnalyticsRemoteConnection(entity.Entity):
    """
    The user experience analyte remote connection entity.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsRemoteConnection and sets the default values.
        """
        super().__init__()
        # The sign in failure percentage of Cloud PC Device. Valid values 0 to 100
        self._cloud_pc_failure_percentage: Optional[float] = None
        # The round tip time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
        self._cloud_pc_round_trip_time: Optional[float] = None
        # The sign in time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
        self._cloud_pc_sign_in_time: Optional[float] = None
        # The core boot time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
        self._core_boot_time: Optional[float] = None
        # The core sign in time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
        self._core_sign_in_time: Optional[float] = None
        # The count of remote connection. Valid values 0 to 2147483647
        self._device_count: Optional[int] = None
        # The id of the device.
        self._device_id: Optional[str] = None
        # The name of the device.
        self._device_name: Optional[str] = None
        # The user experience analytics manufacturer.
        self._manufacturer: Optional[str] = None
        # The user experience analytics device model.
        self._model: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The remote sign in time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
        self._remote_sign_in_time: Optional[float] = None
        # The user experience analytics userPrincipalName.
        self._user_principal_name: Optional[str] = None
        # The user experience analytics virtual network.
        self._virtual_network: Optional[str] = None
    
    @property
    def cloud_pc_failure_percentage(self,) -> Optional[float]:
        """
        Gets the cloudPcFailurePercentage property value. The sign in failure percentage of Cloud PC Device. Valid values 0 to 100
        Returns: Optional[float]
        """
        return self._cloud_pc_failure_percentage
    
    @cloud_pc_failure_percentage.setter
    def cloud_pc_failure_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the cloudPcFailurePercentage property value. The sign in failure percentage of Cloud PC Device. Valid values 0 to 100
        Args:
            value: Value to set for the cloud_pc_failure_percentage property.
        """
        self._cloud_pc_failure_percentage = value
    
    @property
    def cloud_pc_round_trip_time(self,) -> Optional[float]:
        """
        Gets the cloudPcRoundTripTime property value. The round tip time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._cloud_pc_round_trip_time
    
    @cloud_pc_round_trip_time.setter
    def cloud_pc_round_trip_time(self,value: Optional[float] = None) -> None:
        """
        Sets the cloudPcRoundTripTime property value. The round tip time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
        Args:
            value: Value to set for the cloud_pc_round_trip_time property.
        """
        self._cloud_pc_round_trip_time = value
    
    @property
    def cloud_pc_sign_in_time(self,) -> Optional[float]:
        """
        Gets the cloudPcSignInTime property value. The sign in time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._cloud_pc_sign_in_time
    
    @cloud_pc_sign_in_time.setter
    def cloud_pc_sign_in_time(self,value: Optional[float] = None) -> None:
        """
        Sets the cloudPcSignInTime property value. The sign in time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
        Args:
            value: Value to set for the cloud_pc_sign_in_time property.
        """
        self._cloud_pc_sign_in_time = value
    
    @property
    def core_boot_time(self,) -> Optional[float]:
        """
        Gets the coreBootTime property value. The core boot time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._core_boot_time
    
    @core_boot_time.setter
    def core_boot_time(self,value: Optional[float] = None) -> None:
        """
        Sets the coreBootTime property value. The core boot time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
        Args:
            value: Value to set for the core_boot_time property.
        """
        self._core_boot_time = value
    
    @property
    def core_sign_in_time(self,) -> Optional[float]:
        """
        Gets the coreSignInTime property value. The core sign in time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._core_sign_in_time
    
    @core_sign_in_time.setter
    def core_sign_in_time(self,value: Optional[float] = None) -> None:
        """
        Sets the coreSignInTime property value. The core sign in time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
        Args:
            value: Value to set for the core_sign_in_time property.
        """
        self._core_sign_in_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsRemoteConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsRemoteConnection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsRemoteConnection()
    
    @property
    def device_count(self,) -> Optional[int]:
        """
        Gets the deviceCount property value. The count of remote connection. Valid values 0 to 2147483647
        Returns: Optional[int]
        """
        return self._device_count
    
    @device_count.setter
    def device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceCount property value. The count of remote connection. Valid values 0 to 2147483647
        Args:
            value: Value to set for the device_count property.
        """
        self._device_count = value
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The id of the device.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The id of the device.
        Args:
            value: Value to set for the device_id property.
        """
        self._device_id = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The name of the device.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The name of the device.
        Args:
            value: Value to set for the device_name property.
        """
        self._device_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "cloudPcFailurePercentage": lambda n : setattr(self, 'cloud_pc_failure_percentage', n.get_float_value()),
            "cloudPcRoundTripTime": lambda n : setattr(self, 'cloud_pc_round_trip_time', n.get_float_value()),
            "cloudPcSignInTime": lambda n : setattr(self, 'cloud_pc_sign_in_time', n.get_float_value()),
            "coreBootTime": lambda n : setattr(self, 'core_boot_time', n.get_float_value()),
            "coreSignInTime": lambda n : setattr(self, 'core_sign_in_time', n.get_float_value()),
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "remoteSignInTime": lambda n : setattr(self, 'remote_sign_in_time', n.get_float_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "virtualNetwork": lambda n : setattr(self, 'virtual_network', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. The user experience analytics manufacturer.
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. The user experience analytics manufacturer.
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. The user experience analytics device model.
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. The user experience analytics device model.
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
    @property
    def remote_sign_in_time(self,) -> Optional[float]:
        """
        Gets the remoteSignInTime property value. The remote sign in time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._remote_sign_in_time
    
    @remote_sign_in_time.setter
    def remote_sign_in_time(self,value: Optional[float] = None) -> None:
        """
        Sets the remoteSignInTime property value. The remote sign in time of Cloud PC Device. Valid values 0 to 1.79769313486232E+308
        Args:
            value: Value to set for the remote_sign_in_time property.
        """
        self._remote_sign_in_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_float_value("cloudPcFailurePercentage", self.cloud_pc_failure_percentage)
        writer.write_float_value("cloudPcRoundTripTime", self.cloud_pc_round_trip_time)
        writer.write_float_value("cloudPcSignInTime", self.cloud_pc_sign_in_time)
        writer.write_float_value("coreBootTime", self.core_boot_time)
        writer.write_float_value("coreSignInTime", self.core_sign_in_time)
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_float_value("remoteSignInTime", self.remote_sign_in_time)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_str_value("virtualNetwork", self.virtual_network)
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user experience analytics userPrincipalName.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user experience analytics userPrincipalName.
        Args:
            value: Value to set for the user_principal_name property.
        """
        self._user_principal_name = value
    
    @property
    def virtual_network(self,) -> Optional[str]:
        """
        Gets the virtualNetwork property value. The user experience analytics virtual network.
        Returns: Optional[str]
        """
        return self._virtual_network
    
    @virtual_network.setter
    def virtual_network(self,value: Optional[str] = None) -> None:
        """
        Sets the virtualNetwork property value. The user experience analytics virtual network.
        Args:
            value: Value to set for the virtual_network property.
        """
        self._virtual_network = value
    

