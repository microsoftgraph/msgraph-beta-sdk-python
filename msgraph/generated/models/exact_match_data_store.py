from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

exact_match_data_store_base = lazy_import('msgraph.generated.models.exact_match_data_store_base')
exact_match_session = lazy_import('msgraph.generated.models.exact_match_session')

class ExactMatchDataStore(exact_match_data_store_base.ExactMatchDataStoreBase):
    def __init__(self,) -> None:
        """
        Instantiates a new ExactMatchDataStore and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The sessions property
        self._sessions: Optional[List[exact_match_session.ExactMatchSession]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExactMatchDataStore:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExactMatchDataStore
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExactMatchDataStore()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "sessions": lambda n : setattr(self, 'sessions', n.get_collection_of_object_values(exact_match_session.ExactMatchSession)),
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
        writer.write_collection_of_object_values("sessions", self.sessions)
    
    @property
    def sessions(self,) -> Optional[List[exact_match_session.ExactMatchSession]]:
        """
        Gets the sessions property value. The sessions property
        Returns: Optional[List[exact_match_session.ExactMatchSession]]
        """
        return self._sessions
    
    @sessions.setter
    def sessions(self,value: Optional[List[exact_match_session.ExactMatchSession]] = None) -> None:
        """
        Sets the sessions property value. The sessions property
        Args:
            value: Value to set for the sessions property.
        """
        self._sessions = value
    

