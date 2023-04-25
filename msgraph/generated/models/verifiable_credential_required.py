from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import verifiable_credential_requirement_status

from . import verifiable_credential_requirement_status

class VerifiableCredentialRequired(verifiable_credential_requirement_status.VerifiableCredentialRequirementStatus):
    def __init__(self,) -> None:
        """
        Instantiates a new VerifiableCredentialRequired and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.verifiableCredentialRequired"
        # When the presentation request will expire and a new one will need to be generated.
        self._expiry_date_time: Optional[datetime] = None
        # A URL that launches the digital wallet and starts the presentation process. You can present this URL to the user if they can't scan the QR code.
        self._url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VerifiableCredentialRequired:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VerifiableCredentialRequired
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VerifiableCredentialRequired()
    
    @property
    def expiry_date_time(self,) -> Optional[datetime]:
        """
        Gets the expiryDateTime property value. When the presentation request will expire and a new one will need to be generated.
        Returns: Optional[datetime]
        """
        return self._expiry_date_time
    
    @expiry_date_time.setter
    def expiry_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expiryDateTime property value. When the presentation request will expire and a new one will need to be generated.
        Args:
            value: Value to set for the expiry_date_time property.
        """
        self._expiry_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import verifiable_credential_requirement_status

        fields: Dict[str, Callable[[Any], None]] = {
            "expiryDateTime": lambda n : setattr(self, 'expiry_date_time', n.get_datetime_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_datetime_value("expiryDateTime", self.expiry_date_time)
        writer.write_str_value("url", self.url)
    
    @property
    def url(self,) -> Optional[str]:
        """
        Gets the url property value. A URL that launches the digital wallet and starts the presentation process. You can present this URL to the user if they can't scan the QR code.
        Returns: Optional[str]
        """
        return self._url
    
    @url.setter
    def url(self,value: Optional[str] = None) -> None:
        """
        Sets the url property value. A URL that launches the digital wallet and starts the presentation process. You can present this URL to the user if they can't scan the QR code.
        Args:
            value: Value to set for the url property.
        """
        self._url = value
    

