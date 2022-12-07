from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

resultant_app_state = lazy_import('msgraph.generated.models.resultant_app_state')
resultant_app_state_detail = lazy_import('msgraph.generated.models.resultant_app_state_detail')

class MobileAppRelationshipState(AdditionalDataHolder, Parsable):
    """
    Describes the installation status details of the child app in the context of UPN and device id.
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new mobileAppRelationshipState and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The corresponding device id.
        self._device_id: Optional[str] = None
        # The error code for install or uninstall failures of target app.
        self._error_code: Optional[int] = None
        # A list of possible states for application status on an individual device. When devices contact the Intune service and find targeted application enforcement intent, the status of the enforcement is recorded and becomes accessible in the Graph API. Since the application status is identified during device interaction with the Intune service, status records do not immediately appear upon application group assignment; it is created only after the assignment is evaluated in the service and devices start receiving the policy during check-ins.
        self._install_state: Optional[resultant_app_state.ResultantAppState] = None
        # Enum indicating additional details regarding why an application has a particular install state.
        self._install_state_detail: Optional[resultant_app_state_detail.ResultantAppStateDetail] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The collection of source mobile app's ids.
        self._source_ids: Optional[List[str]] = None
        # The related target app's display name.
        self._target_display_name: Optional[str] = None
        # The related target app's id.
        self._target_id: Optional[str] = None
        # The last sync time of the target app.
        self._target_last_sync_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppRelationshipState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppRelationshipState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppRelationshipState()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The corresponding device id.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The corresponding device id.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def error_code(self,) -> Optional[int]:
        """
        Gets the errorCode property value. The error code for install or uninstall failures of target app.
        Returns: Optional[int]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[int] = None) -> None:
        """
        Sets the errorCode property value. The error code for install or uninstall failures of target app.
        Args:
            value: Value to set for the errorCode property.
        """
        self._error_code = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "error_code": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "install_state": lambda n : setattr(self, 'install_state', n.get_enum_value(resultant_app_state.ResultantAppState)),
            "install_state_detail": lambda n : setattr(self, 'install_state_detail', n.get_enum_value(resultant_app_state_detail.ResultantAppStateDetail)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "source_ids": lambda n : setattr(self, 'source_ids', n.get_collection_of_primitive_values(str)),
            "target_display_name": lambda n : setattr(self, 'target_display_name', n.get_str_value()),
            "target_id": lambda n : setattr(self, 'target_id', n.get_str_value()),
            "target_last_sync_date_time": lambda n : setattr(self, 'target_last_sync_date_time', n.get_datetime_value()),
        }
        return fields
    
    @property
    def install_state(self,) -> Optional[resultant_app_state.ResultantAppState]:
        """
        Gets the installState property value. A list of possible states for application status on an individual device. When devices contact the Intune service and find targeted application enforcement intent, the status of the enforcement is recorded and becomes accessible in the Graph API. Since the application status is identified during device interaction with the Intune service, status records do not immediately appear upon application group assignment; it is created only after the assignment is evaluated in the service and devices start receiving the policy during check-ins.
        Returns: Optional[resultant_app_state.ResultantAppState]
        """
        return self._install_state
    
    @install_state.setter
    def install_state(self,value: Optional[resultant_app_state.ResultantAppState] = None) -> None:
        """
        Sets the installState property value. A list of possible states for application status on an individual device. When devices contact the Intune service and find targeted application enforcement intent, the status of the enforcement is recorded and becomes accessible in the Graph API. Since the application status is identified during device interaction with the Intune service, status records do not immediately appear upon application group assignment; it is created only after the assignment is evaluated in the service and devices start receiving the policy during check-ins.
        Args:
            value: Value to set for the installState property.
        """
        self._install_state = value
    
    @property
    def install_state_detail(self,) -> Optional[resultant_app_state_detail.ResultantAppStateDetail]:
        """
        Gets the installStateDetail property value. Enum indicating additional details regarding why an application has a particular install state.
        Returns: Optional[resultant_app_state_detail.ResultantAppStateDetail]
        """
        return self._install_state_detail
    
    @install_state_detail.setter
    def install_state_detail(self,value: Optional[resultant_app_state_detail.ResultantAppStateDetail] = None) -> None:
        """
        Sets the installStateDetail property value. Enum indicating additional details regarding why an application has a particular install state.
        Args:
            value: Value to set for the installStateDetail property.
        """
        self._install_state_detail = value
    
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
        writer.write_str_value("deviceId", self.device_id)
        writer.write_int_value("errorCode", self.error_code)
        writer.write_enum_value("installState", self.install_state)
        writer.write_enum_value("installStateDetail", self.install_state_detail)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("sourceIds", self.source_ids)
        writer.write_str_value("targetDisplayName", self.target_display_name)
        writer.write_str_value("targetId", self.target_id)
        writer.write_datetime_value("targetLastSyncDateTime", self.target_last_sync_date_time)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_ids(self,) -> Optional[List[str]]:
        """
        Gets the sourceIds property value. The collection of source mobile app's ids.
        Returns: Optional[List[str]]
        """
        return self._source_ids
    
    @source_ids.setter
    def source_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the sourceIds property value. The collection of source mobile app's ids.
        Args:
            value: Value to set for the sourceIds property.
        """
        self._source_ids = value
    
    @property
    def target_display_name(self,) -> Optional[str]:
        """
        Gets the targetDisplayName property value. The related target app's display name.
        Returns: Optional[str]
        """
        return self._target_display_name
    
    @target_display_name.setter
    def target_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the targetDisplayName property value. The related target app's display name.
        Args:
            value: Value to set for the targetDisplayName property.
        """
        self._target_display_name = value
    
    @property
    def target_id(self,) -> Optional[str]:
        """
        Gets the targetId property value. The related target app's id.
        Returns: Optional[str]
        """
        return self._target_id
    
    @target_id.setter
    def target_id(self,value: Optional[str] = None) -> None:
        """
        Sets the targetId property value. The related target app's id.
        Args:
            value: Value to set for the targetId property.
        """
        self._target_id = value
    
    @property
    def target_last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the targetLastSyncDateTime property value. The last sync time of the target app.
        Returns: Optional[datetime]
        """
        return self._target_last_sync_date_time
    
    @target_last_sync_date_time.setter
    def target_last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the targetLastSyncDateTime property value. The last sync time of the target app.
        Args:
            value: Value to set for the targetLastSyncDateTime property.
        """
        self._target_last_sync_date_time = value
    

