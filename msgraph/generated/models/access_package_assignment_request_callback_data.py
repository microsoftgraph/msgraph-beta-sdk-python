from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package_custom_extension_stage, custom_extension_data

from . import custom_extension_data

class AccessPackageAssignmentRequestCallbackData(custom_extension_data.CustomExtensionData):
    def __init__(self,) -> None:
        """
        Instantiates a new AccessPackageAssignmentRequestCallbackData and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.accessPackageAssignmentRequestCallbackData"
        # Details for the callback.
        self._custom_extension_stage_instance_detail: Optional[str] = None
        # Unique identifier of the callout to the custom extension.
        self._custom_extension_stage_instance_id: Optional[str] = None
        # Indicates the stage at which the custom callout extension will be executed. The possible values are: assignmentRequestCreated, assignmentRequestApproved, assignmentRequestGranted, assignmentRequestRemoved, assignmentFourteenDaysBeforeExpiration, assignmentOneDayBeforeExpiration, unknownFutureValue.
        self._stage: Optional[access_package_custom_extension_stage.AccessPackageCustomExtensionStage] = None
        # Allow the extension to be able to deny or cancel the request submitted by the requestor. The supported values are Denied and Canceled. This property can only be set for an assignmentRequestCreated stage.
        self._state: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignmentRequestCallbackData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentRequestCallbackData
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAssignmentRequestCallbackData()
    
    @property
    def custom_extension_stage_instance_detail(self,) -> Optional[str]:
        """
        Gets the customExtensionStageInstanceDetail property value. Details for the callback.
        Returns: Optional[str]
        """
        return self._custom_extension_stage_instance_detail
    
    @custom_extension_stage_instance_detail.setter
    def custom_extension_stage_instance_detail(self,value: Optional[str] = None) -> None:
        """
        Sets the customExtensionStageInstanceDetail property value. Details for the callback.
        Args:
            value: Value to set for the custom_extension_stage_instance_detail property.
        """
        self._custom_extension_stage_instance_detail = value
    
    @property
    def custom_extension_stage_instance_id(self,) -> Optional[str]:
        """
        Gets the customExtensionStageInstanceId property value. Unique identifier of the callout to the custom extension.
        Returns: Optional[str]
        """
        return self._custom_extension_stage_instance_id
    
    @custom_extension_stage_instance_id.setter
    def custom_extension_stage_instance_id(self,value: Optional[str] = None) -> None:
        """
        Sets the customExtensionStageInstanceId property value. Unique identifier of the callout to the custom extension.
        Args:
            value: Value to set for the custom_extension_stage_instance_id property.
        """
        self._custom_extension_stage_instance_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package_custom_extension_stage, custom_extension_data

        fields: Dict[str, Callable[[Any], None]] = {
            "customExtensionStageInstanceDetail": lambda n : setattr(self, 'custom_extension_stage_instance_detail', n.get_str_value()),
            "customExtensionStageInstanceId": lambda n : setattr(self, 'custom_extension_stage_instance_id', n.get_str_value()),
            "stage": lambda n : setattr(self, 'stage', n.get_enum_value(access_package_custom_extension_stage.AccessPackageCustomExtensionStage)),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("customExtensionStageInstanceDetail", self.custom_extension_stage_instance_detail)
        writer.write_str_value("customExtensionStageInstanceId", self.custom_extension_stage_instance_id)
        writer.write_enum_value("stage", self.stage)
        writer.write_str_value("state", self.state)
    
    @property
    def stage(self,) -> Optional[access_package_custom_extension_stage.AccessPackageCustomExtensionStage]:
        """
        Gets the stage property value. Indicates the stage at which the custom callout extension will be executed. The possible values are: assignmentRequestCreated, assignmentRequestApproved, assignmentRequestGranted, assignmentRequestRemoved, assignmentFourteenDaysBeforeExpiration, assignmentOneDayBeforeExpiration, unknownFutureValue.
        Returns: Optional[access_package_custom_extension_stage.AccessPackageCustomExtensionStage]
        """
        return self._stage
    
    @stage.setter
    def stage(self,value: Optional[access_package_custom_extension_stage.AccessPackageCustomExtensionStage] = None) -> None:
        """
        Sets the stage property value. Indicates the stage at which the custom callout extension will be executed. The possible values are: assignmentRequestCreated, assignmentRequestApproved, assignmentRequestGranted, assignmentRequestRemoved, assignmentFourteenDaysBeforeExpiration, assignmentOneDayBeforeExpiration, unknownFutureValue.
        Args:
            value: Value to set for the stage property.
        """
        self._stage = value
    
    @property
    def state(self,) -> Optional[str]:
        """
        Gets the state property value. Allow the extension to be able to deny or cancel the request submitted by the requestor. The supported values are Denied and Canceled. This property can only be set for an assignmentRequestCreated stage.
        Returns: Optional[str]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[str] = None) -> None:
        """
        Sets the state property value. Allow the extension to be able to deny or cancel the request submitted by the requestor. The supported values are Denied and Canceled. This property can only be set for an assignmentRequestCreated stage.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

