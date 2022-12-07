from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

managed_device_remote_action = lazy_import('msgraph.generated.models.managed_device_remote_action')

class ExecuteActionPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the executeAction method.
    """
    @property
    def action_name(self,) -> Optional[managed_device_remote_action.ManagedDeviceRemoteAction]:
        """
        Gets the actionName property value. The actionName property
        Returns: Optional[managed_device_remote_action.ManagedDeviceRemoteAction]
        """
        return self._action_name
    
    @action_name.setter
    def action_name(self,value: Optional[managed_device_remote_action.ManagedDeviceRemoteAction] = None) -> None:
        """
        Sets the actionName property value. The actionName property
        Args:
            value: Value to set for the actionName property.
        """
        self._action_name = value
    
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
    def carrier_url(self,) -> Optional[str]:
        """
        Gets the carrierUrl property value. The carrierUrl property
        Returns: Optional[str]
        """
        return self._carrier_url
    
    @carrier_url.setter
    def carrier_url(self,value: Optional[str] = None) -> None:
        """
        Sets the carrierUrl property value. The carrierUrl property
        Args:
            value: Value to set for the carrierUrl property.
        """
        self._carrier_url = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new executeActionPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The actionName property
        self._action_name: Optional[managed_device_remote_action.ManagedDeviceRemoteAction] = None
        # The carrierUrl property
        self._carrier_url: Optional[str] = None
        # The deprovisionReason property
        self._deprovision_reason: Optional[str] = None
        # The deviceIds property
        self._device_ids: Optional[List[str]] = None
        # The deviceName property
        self._device_name: Optional[str] = None
        # The keepEnrollmentData property
        self._keep_enrollment_data: Optional[bool] = None
        # The keepUserData property
        self._keep_user_data: Optional[bool] = None
        # The notificationBody property
        self._notification_body: Optional[str] = None
        # The notificationTitle property
        self._notification_title: Optional[str] = None
        # The organizationalUnitPath property
        self._organizational_unit_path: Optional[str] = None
        # The persistEsimDataPlan property
        self._persist_esim_data_plan: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExecuteActionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExecuteActionPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExecuteActionPostRequestBody()
    
    @property
    def deprovision_reason(self,) -> Optional[str]:
        """
        Gets the deprovisionReason property value. The deprovisionReason property
        Returns: Optional[str]
        """
        return self._deprovision_reason
    
    @deprovision_reason.setter
    def deprovision_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the deprovisionReason property value. The deprovisionReason property
        Args:
            value: Value to set for the deprovisionReason property.
        """
        self._deprovision_reason = value
    
    @property
    def device_ids(self,) -> Optional[List[str]]:
        """
        Gets the deviceIds property value. The deviceIds property
        Returns: Optional[List[str]]
        """
        return self._device_ids
    
    @device_ids.setter
    def device_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the deviceIds property value. The deviceIds property
        Args:
            value: Value to set for the deviceIds property.
        """
        self._device_ids = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The deviceName property
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The deviceName property
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_name": lambda n : setattr(self, 'action_name', n.get_enum_value(managed_device_remote_action.ManagedDeviceRemoteAction)),
            "carrier_url": lambda n : setattr(self, 'carrier_url', n.get_str_value()),
            "deprovision_reason": lambda n : setattr(self, 'deprovision_reason', n.get_str_value()),
            "device_ids": lambda n : setattr(self, 'device_ids', n.get_collection_of_primitive_values(str)),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "keep_enrollment_data": lambda n : setattr(self, 'keep_enrollment_data', n.get_bool_value()),
            "keep_user_data": lambda n : setattr(self, 'keep_user_data', n.get_bool_value()),
            "notification_body": lambda n : setattr(self, 'notification_body', n.get_str_value()),
            "notification_title": lambda n : setattr(self, 'notification_title', n.get_str_value()),
            "organizational_unit_path": lambda n : setattr(self, 'organizational_unit_path', n.get_str_value()),
            "persist_esim_data_plan": lambda n : setattr(self, 'persist_esim_data_plan', n.get_bool_value()),
        }
        return fields
    
    @property
    def keep_enrollment_data(self,) -> Optional[bool]:
        """
        Gets the keepEnrollmentData property value. The keepEnrollmentData property
        Returns: Optional[bool]
        """
        return self._keep_enrollment_data
    
    @keep_enrollment_data.setter
    def keep_enrollment_data(self,value: Optional[bool] = None) -> None:
        """
        Sets the keepEnrollmentData property value. The keepEnrollmentData property
        Args:
            value: Value to set for the keepEnrollmentData property.
        """
        self._keep_enrollment_data = value
    
    @property
    def keep_user_data(self,) -> Optional[bool]:
        """
        Gets the keepUserData property value. The keepUserData property
        Returns: Optional[bool]
        """
        return self._keep_user_data
    
    @keep_user_data.setter
    def keep_user_data(self,value: Optional[bool] = None) -> None:
        """
        Sets the keepUserData property value. The keepUserData property
        Args:
            value: Value to set for the keepUserData property.
        """
        self._keep_user_data = value
    
    @property
    def notification_body(self,) -> Optional[str]:
        """
        Gets the notificationBody property value. The notificationBody property
        Returns: Optional[str]
        """
        return self._notification_body
    
    @notification_body.setter
    def notification_body(self,value: Optional[str] = None) -> None:
        """
        Sets the notificationBody property value. The notificationBody property
        Args:
            value: Value to set for the notificationBody property.
        """
        self._notification_body = value
    
    @property
    def notification_title(self,) -> Optional[str]:
        """
        Gets the notificationTitle property value. The notificationTitle property
        Returns: Optional[str]
        """
        return self._notification_title
    
    @notification_title.setter
    def notification_title(self,value: Optional[str] = None) -> None:
        """
        Sets the notificationTitle property value. The notificationTitle property
        Args:
            value: Value to set for the notificationTitle property.
        """
        self._notification_title = value
    
    @property
    def organizational_unit_path(self,) -> Optional[str]:
        """
        Gets the organizationalUnitPath property value. The organizationalUnitPath property
        Returns: Optional[str]
        """
        return self._organizational_unit_path
    
    @organizational_unit_path.setter
    def organizational_unit_path(self,value: Optional[str] = None) -> None:
        """
        Sets the organizationalUnitPath property value. The organizationalUnitPath property
        Args:
            value: Value to set for the organizationalUnitPath property.
        """
        self._organizational_unit_path = value
    
    @property
    def persist_esim_data_plan(self,) -> Optional[bool]:
        """
        Gets the persistEsimDataPlan property value. The persistEsimDataPlan property
        Returns: Optional[bool]
        """
        return self._persist_esim_data_plan
    
    @persist_esim_data_plan.setter
    def persist_esim_data_plan(self,value: Optional[bool] = None) -> None:
        """
        Sets the persistEsimDataPlan property value. The persistEsimDataPlan property
        Args:
            value: Value to set for the persistEsimDataPlan property.
        """
        self._persist_esim_data_plan = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("actionName", self.action_name)
        writer.write_str_value("carrierUrl", self.carrier_url)
        writer.write_str_value("deprovisionReason", self.deprovision_reason)
        writer.write_collection_of_primitive_values("deviceIds", self.device_ids)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_bool_value("keepEnrollmentData", self.keep_enrollment_data)
        writer.write_bool_value("keepUserData", self.keep_user_data)
        writer.write_str_value("notificationBody", self.notification_body)
        writer.write_str_value("notificationTitle", self.notification_title)
        writer.write_str_value("organizationalUnitPath", self.organizational_unit_path)
        writer.write_bool_value("persistEsimDataPlan", self.persist_esim_data_plan)
        writer.write_additional_data_value(self.additional_data)
    

