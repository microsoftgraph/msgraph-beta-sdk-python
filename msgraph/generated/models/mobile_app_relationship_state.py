from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import resultant_app_state, resultant_app_state_detail

@dataclass
class MobileAppRelationshipState(AdditionalDataHolder, Parsable):
    """
    Describes the installation status details of the child app in the context of UPN and device id. This will be deprecated starting May, 2023 (Intune Release 2305). 
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The corresponding device id.
    device_id: Optional[str] = None
    # The error code for install or uninstall failures of target app.
    error_code: Optional[int] = None
    # A list of possible states for application status on an individual device. When devices contact the Intune service and find targeted application enforcement intent, the status of the enforcement is recorded and becomes accessible in the Graph API. Since the application status is identified during device interaction with the Intune service, status records do not immediately appear upon application group assignment; it is created only after the assignment is evaluated in the service and devices start receiving the policy during check-ins.
    install_state: Optional[resultant_app_state.ResultantAppState] = None
    # Enum indicating additional details regarding why an application has a particular install state.
    install_state_detail: Optional[resultant_app_state_detail.ResultantAppStateDetail] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of source mobile app's ids.
    source_ids: Optional[List[str]] = None
    # The related target app's display name.
    target_display_name: Optional[str] = None
    # The related target app's id.
    target_id: Optional[str] = None
    # The last sync time of the target app.
    target_last_sync_date_time: Optional[datetime] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import resultant_app_state, resultant_app_state_detail

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "installState": lambda n : setattr(self, 'install_state', n.get_enum_value(resultant_app_state.ResultantAppState)),
            "installStateDetail": lambda n : setattr(self, 'install_state_detail', n.get_enum_value(resultant_app_state_detail.ResultantAppStateDetail)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sourceIds": lambda n : setattr(self, 'source_ids', n.get_collection_of_primitive_values(str)),
            "targetDisplayName": lambda n : setattr(self, 'target_display_name', n.get_str_value()),
            "targetId": lambda n : setattr(self, 'target_id', n.get_str_value()),
            "targetLastSyncDateTime": lambda n : setattr(self, 'target_last_sync_date_time', n.get_datetime_value()),
        }
        return fields
    
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
    

