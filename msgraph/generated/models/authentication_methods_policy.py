from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_methods_policy_migration_state, authentication_method_configuration, entity, registration_enforcement, system_credential_preferences

from . import entity

@dataclass
class AuthenticationMethodsPolicy(entity.Entity):
    # Represents the settings for each authentication method. Automatically expanded on GET /policies/authenticationMethodsPolicy.
    authentication_method_configurations: Optional[List[authentication_method_configuration.AuthenticationMethodConfiguration]] = None
    # A description of the policy.
    description: Optional[str] = None
    # The name of the policy.
    display_name: Optional[str] = None
    # The date and time of the last update to the policy.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state of migration of the authentication methods policy from the legacy multifactor authentication and self-service password reset (SSPR) policies. The possible values are: premigration - means the authentication methods policy is used for authentication only, legacy policies are respected. migrationInProgress - means the authentication methods policy is used for both authenication and SSPR, legacy policies are respected. migrationComplete - means the authentication methods policy is used for authentication and SSPR, legacy policies are ignored. unknownFutureValue - Evolvable enumeration sentinel value. Do not use.
    policy_migration_state: Optional[authentication_methods_policy_migration_state.AuthenticationMethodsPolicyMigrationState] = None
    # The version of the policy in use.
    policy_version: Optional[str] = None
    # Days before the user will be asked to reconfirm their method.
    reconfirmation_in_days: Optional[int] = None
    # Enforce registration at sign-in time. This property can be used to remind users to set up targeted authentication methods.
    registration_enforcement: Optional[registration_enforcement.RegistrationEnforcement] = None
    # Prompt users with their most-preferred credential for multifactor authentication.
    system_credential_preferences: Optional[system_credential_preferences.SystemCredentialPreferences] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethodsPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodsPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationMethodsPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_methods_policy_migration_state, authentication_method_configuration, entity, registration_enforcement, system_credential_preferences

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationMethodConfigurations": lambda n : setattr(self, 'authentication_method_configurations', n.get_collection_of_object_values(authentication_method_configuration.AuthenticationMethodConfiguration)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "policyMigrationState": lambda n : setattr(self, 'policy_migration_state', n.get_enum_value(authentication_methods_policy_migration_state.AuthenticationMethodsPolicyMigrationState)),
            "policyVersion": lambda n : setattr(self, 'policy_version', n.get_str_value()),
            "reconfirmationInDays": lambda n : setattr(self, 'reconfirmation_in_days', n.get_int_value()),
            "registrationEnforcement": lambda n : setattr(self, 'registration_enforcement', n.get_object_value(registration_enforcement.RegistrationEnforcement)),
            "systemCredentialPreferences": lambda n : setattr(self, 'system_credential_preferences', n.get_object_value(system_credential_preferences.SystemCredentialPreferences)),
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
        writer.write_collection_of_object_values("authenticationMethodConfigurations", self.authentication_method_configurations)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("policyMigrationState", self.policy_migration_state)
        writer.write_str_value("policyVersion", self.policy_version)
        writer.write_int_value("reconfirmationInDays", self.reconfirmation_in_days)
        writer.write_object_value("registrationEnforcement", self.registration_enforcement)
        writer.write_object_value("systemCredentialPreferences", self.system_credential_preferences)
    

