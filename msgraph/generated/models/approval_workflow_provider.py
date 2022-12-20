from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

business_flow = lazy_import('msgraph.generated.models.business_flow')
entity = lazy_import('msgraph.generated.models.entity')
governance_policy_template = lazy_import('msgraph.generated.models.governance_policy_template')

class ApprovalWorkflowProvider(entity.Entity):
    """
    Provides operations to manage the collection of approvalWorkflowProvider entities.
    """
    @property
    def business_flows(self,) -> Optional[List[business_flow.BusinessFlow]]:
        """
        Gets the businessFlows property value. The businessFlows property
        Returns: Optional[List[business_flow.BusinessFlow]]
        """
        return self._business_flows
    
    @business_flows.setter
    def business_flows(self,value: Optional[List[business_flow.BusinessFlow]] = None) -> None:
        """
        Sets the businessFlows property value. The businessFlows property
        Args:
            value: Value to set for the businessFlows property.
        """
        self._business_flows = value
    
    @property
    def business_flows_with_requests_awaiting_my_decision(self,) -> Optional[List[business_flow.BusinessFlow]]:
        """
        Gets the businessFlowsWithRequestsAwaitingMyDecision property value. The businessFlowsWithRequestsAwaitingMyDecision property
        Returns: Optional[List[business_flow.BusinessFlow]]
        """
        return self._business_flows_with_requests_awaiting_my_decision
    
    @business_flows_with_requests_awaiting_my_decision.setter
    def business_flows_with_requests_awaiting_my_decision(self,value: Optional[List[business_flow.BusinessFlow]] = None) -> None:
        """
        Sets the businessFlowsWithRequestsAwaitingMyDecision property value. The businessFlowsWithRequestsAwaitingMyDecision property
        Args:
            value: Value to set for the businessFlowsWithRequestsAwaitingMyDecision property.
        """
        self._business_flows_with_requests_awaiting_my_decision = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new approvalWorkflowProvider and sets the default values.
        """
        super().__init__()
        # The businessFlows property
        self._business_flows: Optional[List[business_flow.BusinessFlow]] = None
        # The businessFlowsWithRequestsAwaitingMyDecision property
        self._business_flows_with_requests_awaiting_my_decision: Optional[List[business_flow.BusinessFlow]] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The policyTemplates property
        self._policy_templates: Optional[List[governance_policy_template.GovernancePolicyTemplate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApprovalWorkflowProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApprovalWorkflowProvider
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApprovalWorkflowProvider()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "business_flows": lambda n : setattr(self, 'business_flows', n.get_collection_of_object_values(business_flow.BusinessFlow)),
            "business_flows_with_requests_awaiting_my_decision": lambda n : setattr(self, 'business_flows_with_requests_awaiting_my_decision', n.get_collection_of_object_values(business_flow.BusinessFlow)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "policy_templates": lambda n : setattr(self, 'policy_templates', n.get_collection_of_object_values(governance_policy_template.GovernancePolicyTemplate)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def policy_templates(self,) -> Optional[List[governance_policy_template.GovernancePolicyTemplate]]:
        """
        Gets the policyTemplates property value. The policyTemplates property
        Returns: Optional[List[governance_policy_template.GovernancePolicyTemplate]]
        """
        return self._policy_templates
    
    @policy_templates.setter
    def policy_templates(self,value: Optional[List[governance_policy_template.GovernancePolicyTemplate]] = None) -> None:
        """
        Sets the policyTemplates property value. The policyTemplates property
        Args:
            value: Value to set for the policyTemplates property.
        """
        self._policy_templates = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("businessFlows", self.business_flows)
        writer.write_collection_of_object_values("businessFlowsWithRequestsAwaitingMyDecision", self.business_flows_with_requests_awaiting_my_decision)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("policyTemplates", self.policy_templates)
    

