from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class UserTrainingCompletionSummary(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The completedUsersCount property
    completed_users_count: Optional[int] = None
    # The inProgressUsersCount property
    in_progress_users_count: Optional[int] = None
    # The notCompletedUsersCount property
    not_completed_users_count: Optional[int] = None
    # The notStartedUsersCount property
    not_started_users_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The previouslyAssignedUsersCount property
    previously_assigned_users_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserTrainingCompletionSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserTrainingCompletionSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserTrainingCompletionSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "completedUsersCount": lambda n : setattr(self, 'completed_users_count', n.get_int_value()),
            "inProgressUsersCount": lambda n : setattr(self, 'in_progress_users_count', n.get_int_value()),
            "notCompletedUsersCount": lambda n : setattr(self, 'not_completed_users_count', n.get_int_value()),
            "notStartedUsersCount": lambda n : setattr(self, 'not_started_users_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "previouslyAssignedUsersCount": lambda n : setattr(self, 'previously_assigned_users_count', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("completedUsersCount", self.completed_users_count)
        writer.write_int_value("inProgressUsersCount", self.in_progress_users_count)
        writer.write_int_value("notCompletedUsersCount", self.not_completed_users_count)
        writer.write_int_value("notStartedUsersCount", self.not_started_users_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("previouslyAssignedUsersCount", self.previously_assigned_users_count)
        writer.write_additional_data_value(self.additional_data)
    

