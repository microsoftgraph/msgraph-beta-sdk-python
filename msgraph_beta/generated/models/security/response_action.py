from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .allow_file_response_action import AllowFileResponseAction
    from .block_file_response_action import BlockFileResponseAction
    from .collect_investigation_package_response_action import CollectInvestigationPackageResponseAction
    from .disable_user_response_action import DisableUserResponseAction
    from .force_user_password_reset_response_action import ForceUserPasswordResetResponseAction
    from .hard_delete_response_action import HardDeleteResponseAction
    from .initiate_investigation_response_action import InitiateInvestigationResponseAction
    from .isolate_device_response_action import IsolateDeviceResponseAction
    from .mark_user_as_compromised_response_action import MarkUserAsCompromisedResponseAction
    from .move_to_deleted_items_response_action import MoveToDeletedItemsResponseAction
    from .move_to_inbox_response_action import MoveToInboxResponseAction
    from .move_to_junk_response_action import MoveToJunkResponseAction
    from .restrict_app_execution_response_action import RestrictAppExecutionResponseAction
    from .run_antivirus_scan_response_action import RunAntivirusScanResponseAction
    from .soft_delete_response_action import SoftDeleteResponseAction
    from .stop_and_quarantine_file_response_action import StopAndQuarantineFileResponseAction

@dataclass
class ResponseAction(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResponseAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResponseAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.allowFileResponseAction".casefold():
            from .allow_file_response_action import AllowFileResponseAction

            return AllowFileResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.blockFileResponseAction".casefold():
            from .block_file_response_action import BlockFileResponseAction

            return BlockFileResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.collectInvestigationPackageResponseAction".casefold():
            from .collect_investigation_package_response_action import CollectInvestigationPackageResponseAction

            return CollectInvestigationPackageResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.disableUserResponseAction".casefold():
            from .disable_user_response_action import DisableUserResponseAction

            return DisableUserResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.forceUserPasswordResetResponseAction".casefold():
            from .force_user_password_reset_response_action import ForceUserPasswordResetResponseAction

            return ForceUserPasswordResetResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hardDeleteResponseAction".casefold():
            from .hard_delete_response_action import HardDeleteResponseAction

            return HardDeleteResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.initiateInvestigationResponseAction".casefold():
            from .initiate_investigation_response_action import InitiateInvestigationResponseAction

            return InitiateInvestigationResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.isolateDeviceResponseAction".casefold():
            from .isolate_device_response_action import IsolateDeviceResponseAction

            return IsolateDeviceResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.markUserAsCompromisedResponseAction".casefold():
            from .mark_user_as_compromised_response_action import MarkUserAsCompromisedResponseAction

            return MarkUserAsCompromisedResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.moveToDeletedItemsResponseAction".casefold():
            from .move_to_deleted_items_response_action import MoveToDeletedItemsResponseAction

            return MoveToDeletedItemsResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.moveToInboxResponseAction".casefold():
            from .move_to_inbox_response_action import MoveToInboxResponseAction

            return MoveToInboxResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.moveToJunkResponseAction".casefold():
            from .move_to_junk_response_action import MoveToJunkResponseAction

            return MoveToJunkResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.restrictAppExecutionResponseAction".casefold():
            from .restrict_app_execution_response_action import RestrictAppExecutionResponseAction

            return RestrictAppExecutionResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.runAntivirusScanResponseAction".casefold():
            from .run_antivirus_scan_response_action import RunAntivirusScanResponseAction

            return RunAntivirusScanResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.softDeleteResponseAction".casefold():
            from .soft_delete_response_action import SoftDeleteResponseAction

            return SoftDeleteResponseAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.stopAndQuarantineFileResponseAction".casefold():
            from .stop_and_quarantine_file_response_action import StopAndQuarantineFileResponseAction

            return StopAndQuarantineFileResponseAction()
        return ResponseAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .allow_file_response_action import AllowFileResponseAction
        from .block_file_response_action import BlockFileResponseAction
        from .collect_investigation_package_response_action import CollectInvestigationPackageResponseAction
        from .disable_user_response_action import DisableUserResponseAction
        from .force_user_password_reset_response_action import ForceUserPasswordResetResponseAction
        from .hard_delete_response_action import HardDeleteResponseAction
        from .initiate_investigation_response_action import InitiateInvestigationResponseAction
        from .isolate_device_response_action import IsolateDeviceResponseAction
        from .mark_user_as_compromised_response_action import MarkUserAsCompromisedResponseAction
        from .move_to_deleted_items_response_action import MoveToDeletedItemsResponseAction
        from .move_to_inbox_response_action import MoveToInboxResponseAction
        from .move_to_junk_response_action import MoveToJunkResponseAction
        from .restrict_app_execution_response_action import RestrictAppExecutionResponseAction
        from .run_antivirus_scan_response_action import RunAntivirusScanResponseAction
        from .soft_delete_response_action import SoftDeleteResponseAction
        from .stop_and_quarantine_file_response_action import StopAndQuarantineFileResponseAction

        from .allow_file_response_action import AllowFileResponseAction
        from .block_file_response_action import BlockFileResponseAction
        from .collect_investigation_package_response_action import CollectInvestigationPackageResponseAction
        from .disable_user_response_action import DisableUserResponseAction
        from .force_user_password_reset_response_action import ForceUserPasswordResetResponseAction
        from .hard_delete_response_action import HardDeleteResponseAction
        from .initiate_investigation_response_action import InitiateInvestigationResponseAction
        from .isolate_device_response_action import IsolateDeviceResponseAction
        from .mark_user_as_compromised_response_action import MarkUserAsCompromisedResponseAction
        from .move_to_deleted_items_response_action import MoveToDeletedItemsResponseAction
        from .move_to_inbox_response_action import MoveToInboxResponseAction
        from .move_to_junk_response_action import MoveToJunkResponseAction
        from .restrict_app_execution_response_action import RestrictAppExecutionResponseAction
        from .run_antivirus_scan_response_action import RunAntivirusScanResponseAction
        from .soft_delete_response_action import SoftDeleteResponseAction
        from .stop_and_quarantine_file_response_action import StopAndQuarantineFileResponseAction

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_additional_data_value(self.additional_data)
    

