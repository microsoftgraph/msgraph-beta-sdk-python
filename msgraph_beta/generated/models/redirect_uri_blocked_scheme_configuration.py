from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
    from .app_management_restriction_state import AppManagementRestrictionState
    from .redirect_uri_platform_blocked_scheme_configuration import RedirectUriPlatformBlockedSchemeConfiguration

@dataclass
class RedirectUriBlockedSchemeConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The blockedSchemes property
    blocked_schemes: Optional[list[str]] = None
    # The excludeActors property
    exclude_actors: Optional[AppManagementPolicyActorExemptions] = None
    # The exemptFormats property
    exempt_formats: Optional[list[str]] = None
    # The isStateSetByMicrosoft property
    is_state_set_by_microsoft: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The publicClient property
    public_client: Optional[RedirectUriPlatformBlockedSchemeConfiguration] = None
    # The restrictForAppsCreatedAfterDateTime property
    restrict_for_apps_created_after_date_time: Optional[datetime.datetime] = None
    # The spa property
    spa: Optional[RedirectUriPlatformBlockedSchemeConfiguration] = None
    # The state property
    state: Optional[AppManagementRestrictionState] = None
    # The web property
    web: Optional[RedirectUriPlatformBlockedSchemeConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RedirectUriBlockedSchemeConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RedirectUriBlockedSchemeConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RedirectUriBlockedSchemeConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
        from .app_management_restriction_state import AppManagementRestrictionState
        from .redirect_uri_platform_blocked_scheme_configuration import RedirectUriPlatformBlockedSchemeConfiguration

        from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
        from .app_management_restriction_state import AppManagementRestrictionState
        from .redirect_uri_platform_blocked_scheme_configuration import RedirectUriPlatformBlockedSchemeConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "blockedSchemes": lambda n : setattr(self, 'blocked_schemes', n.get_collection_of_primitive_values(str)),
            "excludeActors": lambda n : setattr(self, 'exclude_actors', n.get_object_value(AppManagementPolicyActorExemptions)),
            "exemptFormats": lambda n : setattr(self, 'exempt_formats', n.get_collection_of_primitive_values(str)),
            "isStateSetByMicrosoft": lambda n : setattr(self, 'is_state_set_by_microsoft', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "publicClient": lambda n : setattr(self, 'public_client', n.get_object_value(RedirectUriPlatformBlockedSchemeConfiguration)),
            "restrictForAppsCreatedAfterDateTime": lambda n : setattr(self, 'restrict_for_apps_created_after_date_time', n.get_datetime_value()),
            "spa": lambda n : setattr(self, 'spa', n.get_object_value(RedirectUriPlatformBlockedSchemeConfiguration)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AppManagementRestrictionState)),
            "web": lambda n : setattr(self, 'web', n.get_object_value(RedirectUriPlatformBlockedSchemeConfiguration)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_primitive_values("blockedSchemes", self.blocked_schemes)
        writer.write_object_value("excludeActors", self.exclude_actors)
        writer.write_collection_of_primitive_values("exemptFormats", self.exempt_formats)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("publicClient", self.public_client)
        writer.write_datetime_value("restrictForAppsCreatedAfterDateTime", self.restrict_for_apps_created_after_date_time)
        writer.write_object_value("spa", self.spa)
        writer.write_enum_value("state", self.state)
        writer.write_object_value("web", self.web)
        writer.write_additional_data_value(self.additional_data)
    

