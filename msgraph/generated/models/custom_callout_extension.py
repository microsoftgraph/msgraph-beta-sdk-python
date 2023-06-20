from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package_assignment_request_workflow_extension, access_package_assignment_workflow_extension, custom_access_package_workflow_extension, custom_authentication_extension, custom_extension_authentication_configuration, custom_extension_client_configuration, custom_extension_endpoint_configuration, entity, on_token_issuance_start_custom_extension
    from .identity_governance import custom_task_extension

from . import entity

@dataclass
class CustomCalloutExtension(entity.Entity):
    # Configuration for securing the API call to the logic app. For example, using OAuth client credentials flow.
    authentication_configuration: Optional[custom_extension_authentication_configuration.CustomExtensionAuthenticationConfiguration] = None
    # HTTP connection settings that define how long Azure AD can wait for a connection to a logic app, how many times you can retry a timed-out connection and the exception scenarios when retries are allowed.
    client_configuration: Optional[custom_extension_client_configuration.CustomExtensionClientConfiguration] = None
    # Description for the customCalloutExtension object.
    description: Optional[str] = None
    # Display name for the customCalloutExtension object.
    display_name: Optional[str] = None
    # The type and details for configuring the endpoint to call the logic app's workflow.
    endpoint_configuration: Optional[custom_extension_endpoint_configuration.CustomExtensionEndpointConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomCalloutExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomCalloutExtension
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignmentRequestWorkflowExtension".casefold():
            from . import access_package_assignment_request_workflow_extension

            return access_package_assignment_request_workflow_extension.AccessPackageAssignmentRequestWorkflowExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignmentWorkflowExtension".casefold():
            from . import access_package_assignment_workflow_extension

            return access_package_assignment_workflow_extension.AccessPackageAssignmentWorkflowExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customAccessPackageWorkflowExtension".casefold():
            from . import custom_access_package_workflow_extension

            return custom_access_package_workflow_extension.CustomAccessPackageWorkflowExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customAuthenticationExtension".casefold():
            from . import custom_authentication_extension

            return custom_authentication_extension.CustomAuthenticationExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.customTaskExtension".casefold():
            from .identity_governance import custom_task_extension

            return custom_task_extension.CustomTaskExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onTokenIssuanceStartCustomExtension".casefold():
            from . import on_token_issuance_start_custom_extension

            return on_token_issuance_start_custom_extension.OnTokenIssuanceStartCustomExtension()
        return CustomCalloutExtension()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package_assignment_request_workflow_extension, access_package_assignment_workflow_extension, custom_access_package_workflow_extension, custom_authentication_extension, custom_extension_authentication_configuration, custom_extension_client_configuration, custom_extension_endpoint_configuration, entity, on_token_issuance_start_custom_extension
        from .identity_governance import custom_task_extension

        from . import access_package_assignment_request_workflow_extension, access_package_assignment_workflow_extension, custom_access_package_workflow_extension, custom_authentication_extension, custom_extension_authentication_configuration, custom_extension_client_configuration, custom_extension_endpoint_configuration, entity, on_token_issuance_start_custom_extension
        from .identity_governance import custom_task_extension

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationConfiguration": lambda n : setattr(self, 'authentication_configuration', n.get_object_value(custom_extension_authentication_configuration.CustomExtensionAuthenticationConfiguration)),
            "clientConfiguration": lambda n : setattr(self, 'client_configuration', n.get_object_value(custom_extension_client_configuration.CustomExtensionClientConfiguration)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endpointConfiguration": lambda n : setattr(self, 'endpoint_configuration', n.get_object_value(custom_extension_endpoint_configuration.CustomExtensionEndpointConfiguration)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("authenticationConfiguration", self.authentication_configuration)
        writer.write_object_value("clientConfiguration", self.client_configuration)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("endpointConfiguration", self.endpoint_configuration)
    

