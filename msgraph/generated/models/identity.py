from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import audit_user_identity, azure_communication_services_user_identity, communications_application_identity, communications_application_instance_identity, communications_encrypted_identity, communications_guest_identity, communications_phone_identity, communications_user_identity, email_identity, initiator, program_resource, provisioned_identity, provisioning_service_principal, provisioning_system, service_principal_identity, share_point_identity, teamwork_application_identity, teamwork_conversation_identity, teamwork_tag_identity, teamwork_user_identity, user_identity
    from .security import submission_user_identity

@dataclass
class Identity(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The display name of the identity. Note that this might not always be available or up to date. For example, if a user changes their display name, the API might show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.
    display_name: Optional[str] = None
    # Unique identifier for the identity.
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Identity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Identity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.auditUserIdentity".casefold():
            from . import audit_user_identity

            return audit_user_identity.AuditUserIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureCommunicationServicesUserIdentity".casefold():
            from . import azure_communication_services_user_identity

            return azure_communication_services_user_identity.AzureCommunicationServicesUserIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.communicationsApplicationIdentity".casefold():
            from . import communications_application_identity

            return communications_application_identity.CommunicationsApplicationIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.communicationsApplicationInstanceIdentity".casefold():
            from . import communications_application_instance_identity

            return communications_application_instance_identity.CommunicationsApplicationInstanceIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.communicationsEncryptedIdentity".casefold():
            from . import communications_encrypted_identity

            return communications_encrypted_identity.CommunicationsEncryptedIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.communicationsGuestIdentity".casefold():
            from . import communications_guest_identity

            return communications_guest_identity.CommunicationsGuestIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.communicationsPhoneIdentity".casefold():
            from . import communications_phone_identity

            return communications_phone_identity.CommunicationsPhoneIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.communicationsUserIdentity".casefold():
            from . import communications_user_identity

            return communications_user_identity.CommunicationsUserIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailIdentity".casefold():
            from . import email_identity

            return email_identity.EmailIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.initiator".casefold():
            from . import initiator

            return initiator.Initiator()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.programResource".casefold():
            from . import program_resource

            return program_resource.ProgramResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.provisionedIdentity".casefold():
            from . import provisioned_identity

            return provisioned_identity.ProvisionedIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.provisioningServicePrincipal".casefold():
            from . import provisioning_service_principal

            return provisioning_service_principal.ProvisioningServicePrincipal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.provisioningSystem".casefold():
            from . import provisioning_system

            return provisioning_system.ProvisioningSystem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.submissionUserIdentity".casefold():
            from .security import submission_user_identity

            return submission_user_identity.SubmissionUserIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.servicePrincipalIdentity".casefold():
            from . import service_principal_identity

            return service_principal_identity.ServicePrincipalIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointIdentity".casefold():
            from . import share_point_identity

            return share_point_identity.SharePointIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkApplicationIdentity".casefold():
            from . import teamwork_application_identity

            return teamwork_application_identity.TeamworkApplicationIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkConversationIdentity".casefold():
            from . import teamwork_conversation_identity

            return teamwork_conversation_identity.TeamworkConversationIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkTagIdentity".casefold():
            from . import teamwork_tag_identity

            return teamwork_tag_identity.TeamworkTagIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkUserIdentity".casefold():
            from . import teamwork_user_identity

            return teamwork_user_identity.TeamworkUserIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userIdentity".casefold():
            from . import user_identity

            return user_identity.UserIdentity()
        return Identity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import audit_user_identity, azure_communication_services_user_identity, communications_application_identity, communications_application_instance_identity, communications_encrypted_identity, communications_guest_identity, communications_phone_identity, communications_user_identity, email_identity, initiator, program_resource, provisioned_identity, provisioning_service_principal, provisioning_system, service_principal_identity, share_point_identity, teamwork_application_identity, teamwork_conversation_identity, teamwork_tag_identity, teamwork_user_identity, user_identity
        from .security import submission_user_identity

        from . import audit_user_identity, azure_communication_services_user_identity, communications_application_identity, communications_application_instance_identity, communications_encrypted_identity, communications_guest_identity, communications_phone_identity, communications_user_identity, email_identity, initiator, program_resource, provisioned_identity, provisioning_service_principal, provisioning_system, service_principal_identity, share_point_identity, teamwork_application_identity, teamwork_conversation_identity, teamwork_tag_identity, teamwork_user_identity, user_identity
        from .security import submission_user_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

