from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delegated_privilege_status import DelegatedPrivilegeStatus
    from .tenant_onboarding_eligibility_reason import TenantOnboardingEligibilityReason
    from .tenant_onboarding_status import TenantOnboardingStatus
    from .workload_status import WorkloadStatus

@dataclass
class TenantStatusInformation(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The status of the delegated admin privilege relationship between the managing entity and the managed tenant. Possible values are: none, delegatedAdminPrivileges, unknownFutureValue, granularDelegatedAdminPrivileges, delegatedAndGranularDelegetedAdminPrivileges. You must use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: granularDelegatedAdminPrivileges , delegatedAndGranularDelegetedAdminPrivileges. Optional. Read-only.
    delegated_privilege_status: Optional[DelegatedPrivilegeStatus] = None
    # The date and time the delegated admin privileges status was updated. Optional. Read-only.
    last_delegated_privilege_refresh_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identifier for the account that offboarded the managed tenant. Optional. Read-only.
    offboarded_by_user_id: Optional[str] = None
    # The date and time when the managed tenant was offboarded. Optional. Read-only.
    offboarded_date_time: Optional[datetime.datetime] = None
    # The identifier for the account that onboarded the managed tenant. Optional. Read-only.
    onboarded_by_user_id: Optional[str] = None
    # The date and time when the managed tenant was onboarded. Optional. Read-only.
    onboarded_date_time: Optional[datetime.datetime] = None
    # The onboarding status for the managed tenant.. Possible values are: ineligible, inProcess, active, inactive, unknownFutureValue. Optional. Read-only.
    onboarding_status: Optional[TenantOnboardingStatus] = None
    # Organization's onboarding eligibility reason in Microsoft 365 Lighthouse.. Possible values are: none, contractType, delegatedAdminPrivileges,usersCount,license and unknownFutureValue. Optional. Read-only.
    tenant_onboarding_eligibility_reason: Optional[TenantOnboardingEligibilityReason] = None
    # The collection of workload statues for the managed tenant. Optional. Read-only.
    workload_statuses: Optional[List[WorkloadStatus]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantStatusInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantStatusInformation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TenantStatusInformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .delegated_privilege_status import DelegatedPrivilegeStatus
        from .tenant_onboarding_eligibility_reason import TenantOnboardingEligibilityReason
        from .tenant_onboarding_status import TenantOnboardingStatus
        from .workload_status import WorkloadStatus

        from .delegated_privilege_status import DelegatedPrivilegeStatus
        from .tenant_onboarding_eligibility_reason import TenantOnboardingEligibilityReason
        from .tenant_onboarding_status import TenantOnboardingStatus
        from .workload_status import WorkloadStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "delegatedPrivilegeStatus": lambda n : setattr(self, 'delegated_privilege_status', n.get_enum_value(DelegatedPrivilegeStatus)),
            "lastDelegatedPrivilegeRefreshDateTime": lambda n : setattr(self, 'last_delegated_privilege_refresh_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "offboardedByUserId": lambda n : setattr(self, 'offboarded_by_user_id', n.get_str_value()),
            "offboardedDateTime": lambda n : setattr(self, 'offboarded_date_time', n.get_datetime_value()),
            "onboardedByUserId": lambda n : setattr(self, 'onboarded_by_user_id', n.get_str_value()),
            "onboardedDateTime": lambda n : setattr(self, 'onboarded_date_time', n.get_datetime_value()),
            "onboardingStatus": lambda n : setattr(self, 'onboarding_status', n.get_enum_value(TenantOnboardingStatus)),
            "tenantOnboardingEligibilityReason": lambda n : setattr(self, 'tenant_onboarding_eligibility_reason', n.get_enum_value(TenantOnboardingEligibilityReason)),
            "workloadStatuses": lambda n : setattr(self, 'workload_statuses', n.get_collection_of_object_values(WorkloadStatus)),
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
        writer.write_enum_value("delegatedPrivilegeStatus", self.delegated_privilege_status)
        writer.write_datetime_value("lastDelegatedPrivilegeRefreshDateTime", self.last_delegated_privilege_refresh_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("offboardedByUserId", self.offboarded_by_user_id)
        writer.write_datetime_value("offboardedDateTime", self.offboarded_date_time)
        writer.write_str_value("onboardedByUserId", self.onboarded_by_user_id)
        writer.write_datetime_value("onboardedDateTime", self.onboarded_date_time)
        writer.write_enum_value("onboardingStatus", self.onboarding_status)
        writer.write_enum_value("tenantOnboardingEligibilityReason", self.tenant_onboarding_eligibility_reason)
        writer.write_collection_of_object_values("workloadStatuses", self.workload_statuses)
        writer.write_additional_data_value(self.additional_data)
    

