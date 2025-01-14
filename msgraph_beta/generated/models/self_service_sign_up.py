from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .applied_authentication_event_listener import AppliedAuthenticationEventListener
    from .ciam_user_snapshot import CiamUserSnapshot
    from .entity import Entity
    from .sign_up_identity import SignUpIdentity
    from .sign_up_stage import SignUpStage
    from .sign_up_status import SignUpStatus

from .entity import Entity

@dataclass
class SelfServiceSignUp(Entity, Parsable):
    # The appDisplayName property
    app_display_name: Optional[str] = None
    # The appId property
    app_id: Optional[str] = None
    # The appliedEventListeners property
    applied_event_listeners: Optional[list[AppliedAuthenticationEventListener]] = None
    # The correlationId property
    correlation_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The signUpIdentity property
    sign_up_identity: Optional[SignUpIdentity] = None
    # The signUpIdentityProvider property
    sign_up_identity_provider: Optional[str] = None
    # The signUpStage property
    sign_up_stage: Optional[SignUpStage] = None
    # The status property
    status: Optional[SignUpStatus] = None
    # The userSnapshot property
    user_snapshot: Optional[CiamUserSnapshot] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SelfServiceSignUp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SelfServiceSignUp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SelfServiceSignUp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .applied_authentication_event_listener import AppliedAuthenticationEventListener
        from .ciam_user_snapshot import CiamUserSnapshot
        from .entity import Entity
        from .sign_up_identity import SignUpIdentity
        from .sign_up_stage import SignUpStage
        from .sign_up_status import SignUpStatus

        from .applied_authentication_event_listener import AppliedAuthenticationEventListener
        from .ciam_user_snapshot import CiamUserSnapshot
        from .entity import Entity
        from .sign_up_identity import SignUpIdentity
        from .sign_up_stage import SignUpStage
        from .sign_up_status import SignUpStatus

        fields: dict[str, Callable[[Any], None]] = {
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "appliedEventListeners": lambda n : setattr(self, 'applied_event_listeners', n.get_collection_of_object_values(AppliedAuthenticationEventListener)),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "signUpIdentity": lambda n : setattr(self, 'sign_up_identity', n.get_object_value(SignUpIdentity)),
            "signUpIdentityProvider": lambda n : setattr(self, 'sign_up_identity_provider', n.get_str_value()),
            "signUpStage": lambda n : setattr(self, 'sign_up_stage', n.get_enum_value(SignUpStage)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(SignUpStatus)),
            "userSnapshot": lambda n : setattr(self, 'user_snapshot', n.get_object_value(CiamUserSnapshot)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_collection_of_object_values("appliedEventListeners", self.applied_event_listeners)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("signUpIdentity", self.sign_up_identity)
        writer.write_str_value("signUpIdentityProvider", self.sign_up_identity_provider)
        writer.write_enum_value("signUpStage", self.sign_up_stage)
        writer.write_object_value("status", self.status)
        writer.write_object_value("userSnapshot", self.user_snapshot)
    

