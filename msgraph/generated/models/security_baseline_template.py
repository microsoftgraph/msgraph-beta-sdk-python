from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_template = lazy_import('msgraph.generated.models.device_management_template')
security_baseline_category_state_summary = lazy_import('msgraph.generated.models.security_baseline_category_state_summary')
security_baseline_device_state = lazy_import('msgraph.generated.models.security_baseline_device_state')
security_baseline_state_summary = lazy_import('msgraph.generated.models.security_baseline_state_summary')

class SecurityBaselineTemplate(device_management_template.DeviceManagementTemplate):
    @property
    def category_device_state_summaries(self,) -> Optional[List[security_baseline_category_state_summary.SecurityBaselineCategoryStateSummary]]:
        """
        Gets the categoryDeviceStateSummaries property value. The security baseline per category device state summary
        Returns: Optional[List[security_baseline_category_state_summary.SecurityBaselineCategoryStateSummary]]
        """
        return self._category_device_state_summaries
    
    @category_device_state_summaries.setter
    def category_device_state_summaries(self,value: Optional[List[security_baseline_category_state_summary.SecurityBaselineCategoryStateSummary]] = None) -> None:
        """
        Sets the categoryDeviceStateSummaries property value. The security baseline per category device state summary
        Args:
            value: Value to set for the categoryDeviceStateSummaries property.
        """
        self._category_device_state_summaries = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new SecurityBaselineTemplate and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.securityBaselineTemplate"
        # The security baseline per category device state summary
        self._category_device_state_summaries: Optional[List[security_baseline_category_state_summary.SecurityBaselineCategoryStateSummary]] = None
        # The security baseline device states
        self._device_states: Optional[List[security_baseline_device_state.SecurityBaselineDeviceState]] = None
        # The security baseline device state summary
        self._device_state_summary: Optional[security_baseline_state_summary.SecurityBaselineStateSummary] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecurityBaselineTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecurityBaselineTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SecurityBaselineTemplate()
    
    @property
    def device_states(self,) -> Optional[List[security_baseline_device_state.SecurityBaselineDeviceState]]:
        """
        Gets the deviceStates property value. The security baseline device states
        Returns: Optional[List[security_baseline_device_state.SecurityBaselineDeviceState]]
        """
        return self._device_states
    
    @device_states.setter
    def device_states(self,value: Optional[List[security_baseline_device_state.SecurityBaselineDeviceState]] = None) -> None:
        """
        Sets the deviceStates property value. The security baseline device states
        Args:
            value: Value to set for the deviceStates property.
        """
        self._device_states = value
    
    @property
    def device_state_summary(self,) -> Optional[security_baseline_state_summary.SecurityBaselineStateSummary]:
        """
        Gets the deviceStateSummary property value. The security baseline device state summary
        Returns: Optional[security_baseline_state_summary.SecurityBaselineStateSummary]
        """
        return self._device_state_summary
    
    @device_state_summary.setter
    def device_state_summary(self,value: Optional[security_baseline_state_summary.SecurityBaselineStateSummary] = None) -> None:
        """
        Sets the deviceStateSummary property value. The security baseline device state summary
        Args:
            value: Value to set for the deviceStateSummary property.
        """
        self._device_state_summary = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "category_device_state_summaries": lambda n : setattr(self, 'category_device_state_summaries', n.get_collection_of_object_values(security_baseline_category_state_summary.SecurityBaselineCategoryStateSummary)),
            "device_states": lambda n : setattr(self, 'device_states', n.get_collection_of_object_values(security_baseline_device_state.SecurityBaselineDeviceState)),
            "device_state_summary": lambda n : setattr(self, 'device_state_summary', n.get_object_value(security_baseline_state_summary.SecurityBaselineStateSummary)),
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
        writer.write_collection_of_object_values("categoryDeviceStateSummaries", self.category_device_state_summaries)
        writer.write_collection_of_object_values("deviceStates", self.device_states)
        writer.write_object_value("deviceStateSummary", self.device_state_summary)
    

