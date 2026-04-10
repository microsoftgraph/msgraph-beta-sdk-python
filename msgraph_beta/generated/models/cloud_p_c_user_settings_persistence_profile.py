from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_p_c_user_settings_persistence_profile_status import CloudPCUserSettingsPersistenceProfileStatus

@dataclass
class CloudPCUserSettingsPersistenceProfile(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The last time the user settings persistence profile was attached to the Cloud PC. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    last_profile_attached_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the unique identifier of the Cloud PC user settings persistence profile for the selected Cloud PC user settings persistence. Required. Read-only.
    profile_id: Optional[str] = None
    # Indicates the maximum allowed size in gigabytes of the cloud profile for a specific user. For example, 10 GB of allocated size returns 10 as a response. Required. Read-only.
    profile_size_in_g_b: Optional[int] = None
    # The status property
    status: Optional[CloudPCUserSettingsPersistenceProfileStatus] = None
    # The user principal name of the owner of the cloud profile. For example, connie@contoso.com. Required. Read-only.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPCUserSettingsPersistenceProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPCUserSettingsPersistenceProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPCUserSettingsPersistenceProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_p_c_user_settings_persistence_profile_status import CloudPCUserSettingsPersistenceProfileStatus

        from .cloud_p_c_user_settings_persistence_profile_status import CloudPCUserSettingsPersistenceProfileStatus

        fields: dict[str, Callable[[Any], None]] = {
            "lastProfileAttachedDateTime": lambda n : setattr(self, 'last_profile_attached_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "profileId": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "profileSizeInGB": lambda n : setattr(self, 'profile_size_in_g_b', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CloudPCUserSettingsPersistenceProfileStatus)),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_datetime_value("lastProfileAttachedDateTime", self.last_profile_attached_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("profileId", self.profile_id)
        writer.write_int_value("profileSizeInGB", self.profile_size_in_g_b)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    

