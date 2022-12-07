from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

deployment_state_reason = lazy_import('msgraph.generated.models.windows_updates.deployment_state_reason')
deployment_state_value = lazy_import('msgraph.generated.models.windows_updates.deployment_state_value')
requested_deployment_state_value = lazy_import('msgraph.generated.models.windows_updates.requested_deployment_state_value')

class DeploymentState(AdditionalDataHolder, Parsable):
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
        Instantiates a new deploymentState and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Specifies the reasons the deployment has its state value. Read-only.
        self._reasons: Optional[List[deployment_state_reason.DeploymentStateReason]] = None
        # The requestedValue property
        self._requested_value: Optional[requested_deployment_state_value.RequestedDeploymentStateValue] = None
        # The value property
        self._value: Optional[deployment_state_value.DeploymentStateValue] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeploymentState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeploymentState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeploymentState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reasons": lambda n : setattr(self, 'reasons', n.get_collection_of_object_values(deployment_state_reason.DeploymentStateReason)),
            "requested_value": lambda n : setattr(self, 'requested_value', n.get_enum_value(requested_deployment_state_value.RequestedDeploymentStateValue)),
            "value": lambda n : setattr(self, 'value', n.get_enum_value(deployment_state_value.DeploymentStateValue)),
        }
        return fields
    
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
    
    @property
    def reasons(self,) -> Optional[List[deployment_state_reason.DeploymentStateReason]]:
        """
        Gets the reasons property value. Specifies the reasons the deployment has its state value. Read-only.
        Returns: Optional[List[deployment_state_reason.DeploymentStateReason]]
        """
        return self._reasons
    
    @reasons.setter
    def reasons(self,value: Optional[List[deployment_state_reason.DeploymentStateReason]] = None) -> None:
        """
        Sets the reasons property value. Specifies the reasons the deployment has its state value. Read-only.
        Args:
            value: Value to set for the reasons property.
        """
        self._reasons = value
    
    @property
    def requested_value(self,) -> Optional[requested_deployment_state_value.RequestedDeploymentStateValue]:
        """
        Gets the requestedValue property value. The requestedValue property
        Returns: Optional[requested_deployment_state_value.RequestedDeploymentStateValue]
        """
        return self._requested_value
    
    @requested_value.setter
    def requested_value(self,value: Optional[requested_deployment_state_value.RequestedDeploymentStateValue] = None) -> None:
        """
        Sets the requestedValue property value. The requestedValue property
        Args:
            value: Value to set for the requestedValue property.
        """
        self._requested_value = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("reasons", self.reasons)
        writer.write_enum_value("requestedValue", self.requested_value)
        writer.write_enum_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def value(self,) -> Optional[deployment_state_value.DeploymentStateValue]:
        """
        Gets the value property value. The value property
        Returns: Optional[deployment_state_value.DeploymentStateValue]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[deployment_state_value.DeploymentStateValue] = None) -> None:
        """
        Sets the value property value. The value property
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

