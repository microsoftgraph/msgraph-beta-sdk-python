from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .operation_approval_request_status import OperationApprovalRequestStatus

@dataclass
class OperationApprovalRequestEntityStatus(AdditionalDataHolder, BackedModel, Parsable):
    """
    The operationApprovalRequestEntityStatus complex type is used to provide the basic infortmation relating to the status of a request without revealing too much information to the calling user as it may be an object out of scope.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The status of the Entity connected to the OperationApprovalRequest in regard to changes, whether further requests are allowed or if the Entity is locked. When true, a lock is present on the Entity and no approval requests can be currently made for it. When false, the Entity is not locked and approval requests are allowed. Default value is false. Read-only. This property is read-only.
    entity_locked: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the DateTime when any action on the OperationApprovalRequest is no longer permitted. The value cannot be modified and is automatically populated when the request is created using expiration offset values defined in the service controllers. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only. This property is read-only.
    request_expiration_date_time: Optional[datetime.datetime] = None
    # The unique identifier of the OperationApprovalRequest. This property cannot be modified and is required when the entity status is created. Read-only. This property is read-only.
    request_id: Optional[str] = None
    # Indicates the status of the Approval Request. The status of a request will change when an action is successfully performed on it, such as when it is `approved` or `rejected`, or when the request's expiration DateTime passes and the result is `expired`.
    request_status: Optional[OperationApprovalRequestStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OperationApprovalRequestEntityStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OperationApprovalRequestEntityStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OperationApprovalRequestEntityStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .operation_approval_request_status import OperationApprovalRequestStatus

        from .operation_approval_request_status import OperationApprovalRequestStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "entityLocked": lambda n : setattr(self, 'entity_locked', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "requestExpirationDateTime": lambda n : setattr(self, 'request_expiration_date_time', n.get_datetime_value()),
            "requestId": lambda n : setattr(self, 'request_id', n.get_str_value()),
            "requestStatus": lambda n : setattr(self, 'request_status', n.get_enum_value(OperationApprovalRequestStatus)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("requestStatus", self.request_status)
        writer.write_additional_data_value(self.additional_data)
    

