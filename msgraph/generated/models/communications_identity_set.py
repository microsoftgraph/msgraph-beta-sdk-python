from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

endpoint_type = lazy_import('msgraph.generated.models.endpoint_type')
identity = lazy_import('msgraph.generated.models.identity')
identity_set = lazy_import('msgraph.generated.models.identity_set')

class CommunicationsIdentitySet(identity_set.IdentitySet):
    @property
    def application_instance(self,) -> Optional[identity.Identity]:
        """
        Gets the applicationInstance property value. The application instance associated with this action.
        Returns: Optional[identity.Identity]
        """
        return self._application_instance
    
    @application_instance.setter
    def application_instance(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the applicationInstance property value. The application instance associated with this action.
        Args:
            value: Value to set for the applicationInstance property.
        """
        self._application_instance = value
    
    @property
    def asserted_identity(self,) -> Optional[identity.Identity]:
        """
        Gets the assertedIdentity property value. An identity the participant would like to present itself as to the other participants in the call.
        Returns: Optional[identity.Identity]
        """
        return self._asserted_identity
    
    @asserted_identity.setter
    def asserted_identity(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the assertedIdentity property value. An identity the participant would like to present itself as to the other participants in the call.
        Args:
            value: Value to set for the assertedIdentity property.
        """
        self._asserted_identity = value
    
    @property
    def azure_communication_services_user(self,) -> Optional[identity.Identity]:
        """
        Gets the azureCommunicationServicesUser property value. The Azure Communication Services user associated with this action.
        Returns: Optional[identity.Identity]
        """
        return self._azure_communication_services_user
    
    @azure_communication_services_user.setter
    def azure_communication_services_user(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the azureCommunicationServicesUser property value. The Azure Communication Services user associated with this action.
        Args:
            value: Value to set for the azureCommunicationServicesUser property.
        """
        self._azure_communication_services_user = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CommunicationsIdentitySet and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.communicationsIdentitySet"
        # The application instance associated with this action.
        self._application_instance: Optional[identity.Identity] = None
        # An identity the participant would like to present itself as to the other participants in the call.
        self._asserted_identity: Optional[identity.Identity] = None
        # The Azure Communication Services user associated with this action.
        self._azure_communication_services_user: Optional[identity.Identity] = None
        # The encrypted user associated with this action.
        self._encrypted: Optional[identity.Identity] = None
        # Type of endpoint the participant is using. Possible values are: default, voicemail, skypeForBusiness, skypeForBusinessVoipPhone and unknownFutureValue.
        self._endpoint_type: Optional[endpoint_type.EndpointType] = None
        # The guest user associated with this action.
        self._guest: Optional[identity.Identity] = None
        # The Skype for Business On-Premises user associated with this action.
        self._on_premises: Optional[identity.Identity] = None
        # Inherited from identitySet. The phone user associated with this action.
        self._phone: Optional[identity.Identity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CommunicationsIdentitySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CommunicationsIdentitySet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CommunicationsIdentitySet()
    
    @property
    def encrypted(self,) -> Optional[identity.Identity]:
        """
        Gets the encrypted property value. The encrypted user associated with this action.
        Returns: Optional[identity.Identity]
        """
        return self._encrypted
    
    @encrypted.setter
    def encrypted(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the encrypted property value. The encrypted user associated with this action.
        Args:
            value: Value to set for the encrypted property.
        """
        self._encrypted = value
    
    @property
    def endpoint_type(self,) -> Optional[endpoint_type.EndpointType]:
        """
        Gets the endpointType property value. Type of endpoint the participant is using. Possible values are: default, voicemail, skypeForBusiness, skypeForBusinessVoipPhone and unknownFutureValue.
        Returns: Optional[endpoint_type.EndpointType]
        """
        return self._endpoint_type
    
    @endpoint_type.setter
    def endpoint_type(self,value: Optional[endpoint_type.EndpointType] = None) -> None:
        """
        Sets the endpointType property value. Type of endpoint the participant is using. Possible values are: default, voicemail, skypeForBusiness, skypeForBusinessVoipPhone and unknownFutureValue.
        Args:
            value: Value to set for the endpointType property.
        """
        self._endpoint_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application_instance": lambda n : setattr(self, 'application_instance', n.get_object_value(identity.Identity)),
            "asserted_identity": lambda n : setattr(self, 'asserted_identity', n.get_object_value(identity.Identity)),
            "azure_communication_services_user": lambda n : setattr(self, 'azure_communication_services_user', n.get_object_value(identity.Identity)),
            "encrypted": lambda n : setattr(self, 'encrypted', n.get_object_value(identity.Identity)),
            "endpoint_type": lambda n : setattr(self, 'endpoint_type', n.get_enum_value(endpoint_type.EndpointType)),
            "guest": lambda n : setattr(self, 'guest', n.get_object_value(identity.Identity)),
            "on_premises": lambda n : setattr(self, 'on_premises', n.get_object_value(identity.Identity)),
            "phone": lambda n : setattr(self, 'phone', n.get_object_value(identity.Identity)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def guest(self,) -> Optional[identity.Identity]:
        """
        Gets the guest property value. The guest user associated with this action.
        Returns: Optional[identity.Identity]
        """
        return self._guest
    
    @guest.setter
    def guest(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the guest property value. The guest user associated with this action.
        Args:
            value: Value to set for the guest property.
        """
        self._guest = value
    
    @property
    def on_premises(self,) -> Optional[identity.Identity]:
        """
        Gets the onPremises property value. The Skype for Business On-Premises user associated with this action.
        Returns: Optional[identity.Identity]
        """
        return self._on_premises
    
    @on_premises.setter
    def on_premises(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the onPremises property value. The Skype for Business On-Premises user associated with this action.
        Args:
            value: Value to set for the onPremises property.
        """
        self._on_premises = value
    
    @property
    def phone(self,) -> Optional[identity.Identity]:
        """
        Gets the phone property value. Inherited from identitySet. The phone user associated with this action.
        Returns: Optional[identity.Identity]
        """
        return self._phone
    
    @phone.setter
    def phone(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the phone property value. Inherited from identitySet. The phone user associated with this action.
        Args:
            value: Value to set for the phone property.
        """
        self._phone = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("applicationInstance", self.application_instance)
        writer.write_object_value("assertedIdentity", self.asserted_identity)
        writer.write_object_value("azureCommunicationServicesUser", self.azure_communication_services_user)
        writer.write_object_value("encrypted", self.encrypted)
        writer.write_enum_value("endpointType", self.endpoint_type)
        writer.write_object_value("guest", self.guest)
        writer.write_object_value("onPremises", self.on_premises)
        writer.write_object_value("phone", self.phone)
    

