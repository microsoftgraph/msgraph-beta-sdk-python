from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mailbox_restore_artifact import MailboxRestoreArtifact
    from .restore_session_base import RestoreSessionBase

from .restore_session_base import RestoreSessionBase

@dataclass
class ExchangeRestoreSession(RestoreSessionBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.exchangeRestoreSession"
    # A collection of restore points and destination details that can be used to restore Exchange mailboxes.
    mailbox_restore_artifacts: Optional[List[MailboxRestoreArtifact]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExchangeRestoreSession:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExchangeRestoreSession
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ExchangeRestoreSession()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .mailbox_restore_artifact import MailboxRestoreArtifact
        from .restore_session_base import RestoreSessionBase

        from .mailbox_restore_artifact import MailboxRestoreArtifact
        from .restore_session_base import RestoreSessionBase

        fields: Dict[str, Callable[[Any], None]] = {
            "mailboxRestoreArtifacts": lambda n : setattr(self, 'mailbox_restore_artifacts', n.get_collection_of_object_values(MailboxRestoreArtifact)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("mailboxRestoreArtifacts", self.mailbox_restore_artifacts)
    

