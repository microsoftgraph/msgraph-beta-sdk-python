from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import audit_user_identity, azure_communication_services_user_identity, communications_application_identity, communications_application_instance_identity, communications_encrypted_identity, communications_guest_identity, communications_phone_identity, communications_user_identity, email_identity, initiator, program_resource, provisioned_identity, provisioning_service_principal, provisioning_system, service_principal_identity, share_point_identity, teamwork_application_identity, teamwork_conversation_identity, teamwork_tag_identity, teamwork_user_identity, user_identity
    from .security import submission_user_identity

class Identity(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new identity and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The display name of the identity. This property is read-only.
        self._display_name: Optional[str] = None
        # The identifier of the identity. This property is read-only.
        self._id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Identity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Identity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.auditUserIdentity":
                from . import audit_user_identity

                return audit_user_identity.AuditUserIdentity()
            if mapping_value == "#microsoft.graph.azureCommunicationServicesUserIdentity":
                from . import azure_communication_services_user_identity

                return azure_communication_services_user_identity.AzureCommunicationServicesUserIdentity()
            if mapping_value == "#microsoft.graph.communicationsApplicationIdentity":
                from . import communications_application_identity

                return communications_application_identity.CommunicationsApplicationIdentity()
            if mapping_value == "#microsoft.graph.communicationsApplicationInstanceIdentity":
                from . import communications_application_instance_identity

                return communications_application_instance_identity.CommunicationsApplicationInstanceIdentity()
            if mapping_value == "#microsoft.graph.communicationsEncryptedIdentity":
                from . import communications_encrypted_identity

                return communications_encrypted_identity.CommunicationsEncryptedIdentity()
            if mapping_value == "#microsoft.graph.communicationsGuestIdentity":
                from . import communications_guest_identity

                return communications_guest_identity.CommunicationsGuestIdentity()
            if mapping_value == "#microsoft.graph.communicationsPhoneIdentity":
                from . import communications_phone_identity

                return communications_phone_identity.CommunicationsPhoneIdentity()
            if mapping_value == "#microsoft.graph.communicationsUserIdentity":
                from . import communications_user_identity

                return communications_user_identity.CommunicationsUserIdentity()
            if mapping_value == "#microsoft.graph.emailIdentity":
                from . import email_identity

                return email_identity.EmailIdentity()
            if mapping_value == "#microsoft.graph.initiator":
                from . import initiator

                return initiator.Initiator()
            if mapping_value == "#microsoft.graph.programResource":
                from . import program_resource

                return program_resource.ProgramResource()
            if mapping_value == "#microsoft.graph.provisionedIdentity":
                from . import provisioned_identity

                return provisioned_identity.ProvisionedIdentity()
            if mapping_value == "#microsoft.graph.provisioningServicePrincipal":
                from . import provisioning_service_principal

                return provisioning_service_principal.ProvisioningServicePrincipal()
            if mapping_value == "#microsoft.graph.provisioningSystem":
                from . import provisioning_system

                return provisioning_system.ProvisioningSystem()
            if mapping_value == "#microsoft.graph.security.submissionUserIdentity":
                from .security import submission_user_identity

                return submission_user_identity.SubmissionUserIdentity()
            if mapping_value == "#microsoft.graph.servicePrincipalIdentity":
                from . import service_principal_identity

                return service_principal_identity.ServicePrincipalIdentity()
            if mapping_value == "#microsoft.graph.sharePointIdentity":
                from . import share_point_identity

                return share_point_identity.SharePointIdentity()
            if mapping_value == "#microsoft.graph.teamworkApplicationIdentity":
                from . import teamwork_application_identity

                return teamwork_application_identity.TeamworkApplicationIdentity()
            if mapping_value == "#microsoft.graph.teamworkConversationIdentity":
                from . import teamwork_conversation_identity

                return teamwork_conversation_identity.TeamworkConversationIdentity()
            if mapping_value == "#microsoft.graph.teamworkTagIdentity":
                from . import teamwork_tag_identity

                return teamwork_tag_identity.TeamworkTagIdentity()
            if mapping_value == "#microsoft.graph.teamworkUserIdentity":
                from . import teamwork_user_identity

                return teamwork_user_identity.TeamworkUserIdentity()
            if mapping_value == "#microsoft.graph.userIdentity":
                from . import user_identity

                return user_identity.UserIdentity()
        return Identity()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the identity. This property is read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the identity. This property is read-only.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import audit_user_identity, azure_communication_services_user_identity, communications_application_identity, communications_application_instance_identity, communications_encrypted_identity, communications_guest_identity, communications_phone_identity, communications_user_identity, email_identity, initiator, program_resource, provisioned_identity, provisioning_service_principal, provisioning_system, service_principal_identity, share_point_identity, teamwork_application_identity, teamwork_conversation_identity, teamwork_tag_identity, teamwork_user_identity, user_identity
        from .security import submission_user_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The identifier of the identity. This property is read-only.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The identifier of the identity. This property is read-only.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

