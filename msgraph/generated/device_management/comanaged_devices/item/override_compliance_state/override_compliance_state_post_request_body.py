from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import administrator_configured_device_compliance_state

class OverrideComplianceStatePostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new overrideComplianceStatePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Administrator configured device compliance state Enum
        self._compliance_state: Optional[administrator_configured_device_compliance_state.AdministratorConfiguredDeviceComplianceState] = None
        # The remediationUrl property
        self._remediation_url: Optional[str] = None
    
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
    def compliance_state(self,) -> Optional[administrator_configured_device_compliance_state.AdministratorConfiguredDeviceComplianceState]:
        """
        Gets the complianceState property value. Administrator configured device compliance state Enum
        Returns: Optional[administrator_configured_device_compliance_state.AdministratorConfiguredDeviceComplianceState]
        """
        return self._compliance_state
    
    @compliance_state.setter
    def compliance_state(self,value: Optional[administrator_configured_device_compliance_state.AdministratorConfiguredDeviceComplianceState] = None) -> None:
        """
        Sets the complianceState property value. Administrator configured device compliance state Enum
        Args:
            value: Value to set for the compliance_state property.
        """
        self._compliance_state = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OverrideComplianceStatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OverrideComplianceStatePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OverrideComplianceStatePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models import administrator_configured_device_compliance_state

        fields: Dict[str, Callable[[Any], None]] = {
            "complianceState": lambda n : setattr(self, 'compliance_state', n.get_enum_value(administrator_configured_device_compliance_state.AdministratorConfiguredDeviceComplianceState)),
            "remediationUrl": lambda n : setattr(self, 'remediation_url', n.get_str_value()),
        }
        return fields
    
    @property
    def remediation_url(self,) -> Optional[str]:
        """
        Gets the remediationUrl property value. The remediationUrl property
        Returns: Optional[str]
        """
        return self._remediation_url
    
    @remediation_url.setter
    def remediation_url(self,value: Optional[str] = None) -> None:
        """
        Sets the remediationUrl property value. The remediationUrl property
        Args:
            value: Value to set for the remediation_url property.
        """
        self._remediation_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("complianceState", self.compliance_state)
        writer.write_str_value("remediationUrl", self.remediation_url)
        writer.write_additional_data_value(self.additional_data)
    

