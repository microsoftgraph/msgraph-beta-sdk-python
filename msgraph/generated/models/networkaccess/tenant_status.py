from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import onboarding_status
    from .. import entity

from .. import entity

@dataclass
class TenantStatus(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The onboardingErrorMessage property
    onboarding_error_message: Optional[str] = None
    # The onboardingStatus property
    onboarding_status: Optional[onboarding_status.OnboardingStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TenantStatus
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TenantStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import onboarding_status
        from .. import entity

        from . import onboarding_status
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "onboardingErrorMessage": lambda n : setattr(self, 'onboarding_error_message', n.get_str_value()),
            "onboardingStatus": lambda n : setattr(self, 'onboarding_status', n.get_enum_value(onboarding_status.OnboardingStatus)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("onboardingErrorMessage", self.onboarding_error_message)
        writer.write_enum_value("onboardingStatus", self.onboarding_status)
    

